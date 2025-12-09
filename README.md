# 📘 RAG-sync — PDF Retrieval-Augmented Generation System

RAG-sync is a simple end-to-end **Retrieval-Augmented Generation (RAG)** pipeline that takes PDF documents, converts them into embeddings, stores them in a local vector database, and retrieves the most relevant chunks to answer user queries using an AI model.

---

## 🔄 How RAG Works (Quick Overview)

RAG has **two phases**:

### 1️⃣ Indexing Phase (Data Injection)
- **Load PDFs**  
- **Chunk text** to maintain context  
- **Generate embeddings** using Sentence-Transformers (`all-MiniLM-L6-v2`)  
- **Store vectors** in ChromaDB for fast similarity search  

### 2️⃣ Retrieving Phase (User Query → Answer)
- Convert query → embedding  
- Search similar chunks in vector DB  
- Select top relevant context  
- Provide context + question to an LLM  
- Generate grounded, accurate answers  

---

## 🗄️ Vector Database Used
**ChromaDB** — lightweight, local, fast, ideal for learning and small projects.

Other popular options: Pinecone, Qdrant, Weaviate, Milvus, FAISS.

---

## ⚙️ LangChain Usage
LangChain simplifies:
- Loading & splitting documents  
- Creating embeddings  
- Connecting to vector DB  
- Running retrieval pipelines  

---

## 🚀 How to Run

### Install dependencies:
pip install langchain chromadb sentence-transformers pypdf

### Run Indexing:
python indexing.py

### Run Retrieval:
python retriving.py
---
## 📌 Note
`local_chroma_db/` is ignored in Git because it contains heavy vector files.

---

## 👤 Author
Sujit Sadalage

## 📁 Project Structure

RAG-sync/
│
├── Data_Injection and Data_Retrieval/
│ ├── indexing.py # Convert PDF → chunks → embeddings → DB
│ ├── retriving.py # Query search + context retrieval
│ └── local_chroma_db/ # Auto-generated vector DB (ignored)
│
├── blackbook.pdf
└── README.md


