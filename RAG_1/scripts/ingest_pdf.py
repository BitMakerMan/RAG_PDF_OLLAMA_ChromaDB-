#from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb
import os

# Configurazioni
PDF_PATH = "../data/documento.pdf"
CHROMA_PATH = "../db"

def ingest_pdf(pdf_path):
    # 1. Carica il PDF
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()

    # 2. Chunkizza
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(pages)

    # 3. Genera embedding
    model = SentenceTransformer('BAAI/bge-small-en-v1.5')
    texts = [doc.page_content for doc in docs]
    embeddings = model.encode(texts)

    # 4. Salva in ChromaDB
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection_name = "pdf_chunks"

    try:
        client.delete_collection(collection_name)
    except:
        pass

    collection = client.get_or_create_collection(name=collection_name)

    ids = [f"id_{i}" for i in range(len(embeddings))]
    metadatas = [{"source": doc.metadata.get("source")} for doc in docs]

    collection.add(
        embeddings=embeddings.tolist(),
        documents=texts,
        metadatas=metadatas,
        ids=ids
    )

    print(f"Ingest completato: {len(docs)} chunk salvati.")

if __name__ == "__main__":
    pdf_path = input("Inserisci il percorso del PDF da processare: ")
    if os.path.exists(pdf_path):
        ingest_pdf(pdf_path)
    else:
        print("File non trovato.")