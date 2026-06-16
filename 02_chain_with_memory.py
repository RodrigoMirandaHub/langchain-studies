<<<<<<< HEAD
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente prestativo."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | llm

store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

config = {"configurable": {"session_id": "sessao_01"}}

r1 = with_memory.invoke({"input": "Meu nome é Rodrigo e trabalho com automação"}, config=config)
print("R1:", r1.content)

r2 = with_memory.invoke({"input": "Qual é o meu nome e o que eu faço?"}, config=config)
=======
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.7)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente prestativo."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | llm

store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

config = {"configurable": {"session_id": "sessao_01"}}

r1 = with_memory.invoke({"input": "Meu nome é Rodrigo e trabalho com automação"}, config=config)
print("R1:", r1.content)

r2 = with_memory.invoke({"input": "Qual é o meu nome e o que eu faço?"}, config=config)
>>>>>>> b2ec4cdea7d662fb98737ccaf8d5cb7a02191f77
print("R2:", r2.content)