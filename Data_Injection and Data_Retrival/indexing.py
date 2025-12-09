from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma





# LOADING
# Path to your PDF
pdf_path = r"C:\Users\sujit\Music\Downloads\turtle-crossing-start\pythonProject1\AIAgentic\RAG\blackbook.pdf"
# Create a loader instance
loader = PyPDFLoader(pdf_path)
# Load all pages as documents
document= loader.load()
# # Print the content of the first page :array of pages
# print(docs[0].page_content)




# SPLITTING
text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,   # number of characters per chunk
    chunk_overlap=50  # # overlap to preserve context
)
# Split documents into smaller chunks
chunks = text_splitter.split_documents(document)
texts = [chunk.page_content for chunk in chunks]






# VECTOR EMBEDDINGS
# model for creating embeddings (numerical values)
embedding_function = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)





# STORING IN QDRANT LOCALLY
vector_store = Chroma.from_texts(
    texts=texts,
    embedding=embedding_function,
    persist_directory="local_chroma_db"  # folder will be created
)

print("✅ Embeddings stored using ChromaDB!")








