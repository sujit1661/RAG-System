# 📘 RAG-sync — PDF Retrieval-Augmented Generation System

RAG-sync is a simple end-to-end **Retrieval-Augmented Generation (RAG)** system that allows you to ask questions from PDF documents using an AI model.  
It converts PDFs into embeddings, stores them in a local vector database, and retrieves the most relevant chunks to generate accurate, grounded answers.

---

## 🔄 How RAG Works (Quick Overview)

RAG works in **two main phases**:

### 1️⃣ Data Injection (Indexing Phase)
- Load PDF documents  
- Split text into meaningful chunks  
- Generate embeddings using Sentence Transformers  
- Store embeddings in a local vector database (ChromaDB)  

### 2️⃣ Data Retrieval (Query Phase)
- Convert user query into an embedding  
- Perform similarity search in vector DB  
- Retrieve the most relevant text chunks  
- Pass retrieved context to the LLM  
- Generate an accurate, context-aware answer  

---

## 🗄️ Vector Database
**ChromaDB** is used as the local vector store.

Why ChromaDB?
- Lightweight & fast  
- Runs locally  
- Easy to integrate with LangChain  
- Perfect for learning & small-scale RAG systems  

Other popular vector DBs:
- Pinecone  
- Qdrant  
- Weaviate  
- Milvus  
- FAISS  

---

## ⚙️ LangChain Role
LangChain helps simplify:
- PDF loading  
- Text chunking  
- Embedding generation  
- Vector database interaction  
- Retrieval pipeline orchestration  

---

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install langchain chromadb sentence-transformers pypdf
```

### 2️⃣ Run Data Injection (Indexing)
```bash
python indexing.py
```

This will:
- Read `blackbook.pdf`
- Create embeddings
- Store them in `local_chroma_db/`

### 3️⃣ Run Data Retrieval
```bash
python retriving.py
```

Ask questions and get answers directly from the PDF content.

---

## 📌 Important Notes
- `local_chroma_db/` is **auto-generated** and ignored in Git (`.gitignore`)
- Large vector files are not committed to the repository
- You can replace `blackbook.pdf` with any PDF of your choice

---

## 📁 Project Structure

```
RAG-sync/
│
├── Data_Injection and Data_Retrival/
│   ├── indexing.py        # PDF → chunks → embeddings → vector DB
│   ├── retriving.py       # Query → similarity search → answer
│   └── local_chroma_db/   # Auto-generated vector database (ignored)
│
├── blackbook.pdf          # Input PDF document
├── notes                  # Optional notes / experiments
└── .gitignore
```

---

## 👤 Author
**Sujit Sadalage**

---

## ⭐ Future Improvements
- Add FastAPI / Flask API layer  
- Add chat UI (Streamlit / React)  
- Support multiple PDFs  
- Add metadata filtering  
- Plug in different LLM providers  

---

⭐ If you found this useful, consider starring the repo!
