# 📄 RAG PDF Analyzer with Ollama, Qwen3:8b & ChromaDB  
*Un sistema RAG (Retrieval-Augmented Generation) per analizzare PDF con intelligenza artificiale, tutto in locale.*

---

## 🧠 Descrizione
Questo progetto implementa un sistema **RAG locale** che permette di:
- **Leggere PDF** estrarre il testo  
- **Chunkizzare** il contenuto  
- **Generare embedding** con modelli open-source  
- **Archiviare i dati** in un database vettoriale (ChromaDB)  
- **Rispondere a domande** usando Qwen3:8b su Ollama  

L'intero sistema è eseguibile in locale, senza dipendenze cloud, ed è ideale per analisi di contratti, documenti tecnici, manuali e altro.

---

## ✨ Funzionalità
- ✅ Estrazione testo da PDF  
- ✅ Chunking avanzato con `RecursiveCharacterTextSplitter`  
- ✅ Generazione embedding con `BAAI/bge-small-en-v1.5`  
- ✅ Database vettoriale locale con **ChromaDB**  
- ✅ Query semantica + risposta contestuale con **Qwen3:8b** su **Ollama**  
- ✅ Integrazione con **n8n** per automazioni  

---

## 🛠 Requisiti
- **Python 3.9+**  
- **Ollama** (con `qwen3:8b` installato)  
- Librerie Python:
  ```bash
  pip install langchain langchain-community pypdf sentence-transformers chromadb requests
  ```

Se i tuoi PDF sono in italiano o misti:
  ```bash
  pip install sentence-transformers
  ```

---

## 📁 Struttura del Progetto
```
RAG_1/
├── data/              # PDF caricati
├── scripts/             # Script Python
│   ├── ingest_pdf.py    # Inserisce PDF nel RAG
│   └── rag_query.py     # Fai domande al sistema
├── db/                  # Dati di ChromaDB
└── README.md            # Documentazione
```

---

## 🚀 Setup Rapido

### 1. Scarica Qwen3:8b su Ollama
```bash
ollama pull qwen3:8b
```

### 2. Crea l'ambiente virtuale
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Installa dipendenze
```bash
pip install langchain langchain-community pypdf sentence-transformers chromadb requests
```

### 4. Crea la struttura delle cartelle
```bash
mkdir -p data scripts db
```

### 5. Copia gli script
Incolla `ingest_pdf.py` e `rag_query.py` nella cartella `scripts/`.

---

## 📥 Inserisci un PDF nel sistema
```bash
cd scripts
python ingest_pdf.py
```
Inserisci il percorso del PDF quando richiesto.

---

## 💬 Fai una domanda al documento
```bash
python rag_query.py
```
Esempio di domanda:
```
Qual è la durata del contratto?
```

---

## 🔧 Integrazione con n8n (Opzionale)
Puoi integrare il sistema con **n8n** per:
- Ricevere PDF via Webhook  
- Automatizzare l'ingestione  
- Inviare risposte via email/slack/notion  

Esempio di workflow:
```
HTTP Webhook → File System Watcher → Python Script (ingest_pdf.py) → Ollama Response
```

## 🛠 Personalizzazioni Possibili
- Cambiare modello LLM (es. `llama3`, `mistral`, ecc.)  
- Usare modelli multilingua per embedding  
- Aggiungere interfaccia grafica (Tkinter, Streamlit)  
- Automatizzare il caricamento di più PDF  
- Integrare con GUI desktop/web
