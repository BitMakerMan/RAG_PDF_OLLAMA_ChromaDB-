from sentence_transformers import SentenceTransformer
import chromadb
import requests

CHROMA_PATH = "../db"

def ask_rag(question):
    # 1. Genera embedding della domanda
    model = SentenceTransformer('BAAI/bge-small-en-v1.5')
    question_embedding = model.encode([question])

    # 2. Cerca chunk simili
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_collection(name="pdf_chunks")

    results = collection.query(
        query_embeddings=question_embedding.tolist(),
        n_results=3
    )

    relevant_texts = results['documents'][0]

    # 3. Crea prompt contestuale
    context = "\n".join(relevant_texts)
    prompt = f"""
Sei un assistente AI specializzato nell'analisi di documenti.
Usa il seguente contesto per rispondere alla domanda.

Contesto:
{context}

Domanda:
{question}
"""

    # 4. Chiedi a Ollama
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "qwen3:8b",
        "prompt": prompt,
        "stream": False
    })

    return response.json()['response']

if __name__ == "__main__":
    question = input("Fai una domanda sul documento: ")
    answer = ask_rag(question)
    print("\nRisposta:")
    print(answer)