import csv
csv.field_size_limit(10_000_000)

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate

load_dotenv()

# 1. Carregar o documento
loader = TextLoader("knowledge_base.txt", encoding="utf-8")
documents = loader.load()

# 2. Quebrar em pedaços (chunks)
splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
chunks = splitter.split_documents(documents)
print(f"Total de chunks criados: {len(chunks)}")

# 3. Gerar embeddings e indexar no Chroma
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(chunks, embeddings)

# 4. Criar retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# 5. Montar o RAG manualmente
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
Responda à pergunta usando APENAS o contexto abaixo. Se não souber, diga que não sabe.

Contexto:
{context}

Pergunta: {question}

Resposta:
"""
)

rag_chain = prompt | llm

def ask(question):
    docs = retriever.invoke(question)
    context = "\n".join([d.page_content for d in docs])
    result = rag_chain.invoke({"context": context, "question": question})
    print(f"\nPergunta: {question}")
    print(f"Resposta: {result.content}")
    print(f"\nFontes usadas: {[d.page_content[:50] + '...' for d in docs]}")

# Testes
ask("Quanto custa o plano Pro?")
ask("Qual é o rate limit da API no plano gratuito?")
ask("Quais eventos disparam webhooks?")