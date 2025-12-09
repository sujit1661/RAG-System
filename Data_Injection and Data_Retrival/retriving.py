from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from openai import OpenAI


# take user query
user=input("->")

# convert it into embeddings
embedding_model=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load your existing Chroma DB
vectorDb=Chroma(
    persist_directory="local_chroma_db",
    embedding_function=embedding_model
)

# Retrieve relevant chunks(If your database has 100 document chunks,
# Chroma will rank all of them by similarity to your query and return the top 5.)
results = vectorDb.similarity_search(
    query=user,
    k=5         # k is the number of results you want to retrieve.
)

# store
context_text = "\n".join([f"- {doc.page_content}" for doc in results])


SYSTEM_PROMPT = f"""You are an AI Researcher and assistant. 
Your task is to answer the user's question strictly based on the provided context chunks from the document.
Instructions:
1. Use ONLY the information provided in the "Context" section below.
2. Do not use outside knowledge or hallucinate facts.
3. If the answer is not found in the context, explicitly say: "I cannot find the answer in the provided document chunks."
4. If the context contains multiple relevant points, format your answer as a bulleted list.
5. Keep the tone professional and concise.
Context:
{context_text}
User Question:
{user}
"""


# use LLM to give proper response
client = OpenAI(
    api_key="YOUR_API",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[

        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user}
    ]
)

print(f"your result:\n {response.choices[0].message.content}")
