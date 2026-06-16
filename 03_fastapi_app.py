from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

app = FastAPI(title="Lead Qualifier API")

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

prompt = PromptTemplate(
    input_variables=["lead_name", "company", "message"],
    template="""
Você é um qualificador de leads B2B. Analise o lead abaixo e responda em JSON.

Nome: {lead_name}
Empresa: {company}
Mensagem: {message}

Responda APENAS com JSON:
{{"score": 1-10, "intent": "alta|media|baixa", "reason": "motivo em 1 frase"}}
"""
)

chain = prompt | llm


class Lead(BaseModel):
    lead_name: str
    company: str
    message: str


@app.get("/")
def root():
    return {"status": "API rodando"}


@app.post("/qualify")
def qualify_lead(lead: Lead):
    result = chain.invoke({
        "lead_name": lead.lead_name,
        "company": lead.company,
        "message": lead.message
    })
    return {"result": result.content}