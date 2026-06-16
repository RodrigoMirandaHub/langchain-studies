<<<<<<< HEAD
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate


load_dotenv()

llm= ChatGroq (model="llama-3.1-8b-instant", temperature=0)

prompt = PromptTemplate(
    input_variables=["lead_name", "company", "message"],
    template="""
Você é um qualificador de leads B2B. Analise o lead abaixo e responda em JSON.

Nome : {lead_name}
Empresa: {company}
Mensagem: {message}

Responda APENAS com JSON:
{{"score": 1-10, "intent": "alta|media|baixa", "reason": "motivo em 1 frase"}}
"""

)

chain = prompt | llm

result = chain.invoke({
    "lead_name": "Carlos Silva",
    "company": "TechCorp",
    "message": "Preciso automatizar meu processo de vendas urgente, temos budget aprovado"
})

=======
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate


load_dotenv()

llm= ChatGroq (model="llama-3.1-8b-instant", temperature=0)

prompt = PromptTemplate(
    input_variables=["lead_name", "company", "message"],
    template="""
Você é um qualificador de leads B2B. Analise o lead abaixo e responda em JSON.

Nome : {lead_name}
Empresa: {company}
Mensagem: {message}

Responda APENAS com JSON:
{{"score": 1-10, "intent": "alta|media|baixa", "reason": "motivo em 1 frase"}}
"""

)

chain = prompt | llm

result = chain.invoke({
    "lead_name": "Carlos Silva",
    "company": "TechCorp",
    "message": "Preciso automatizar meu processo de vendas urgente, temos budget aprovado"
})

>>>>>>> b2ec4cdea7d662fb98737ccaf8d5cb7a02191f77
print (result.content)