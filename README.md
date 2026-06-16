# LangChain Studies

Repositório de estudos práticos com LangChain, LangGraph e IA aplicada.
Cada pasta é um projeto ou conceito independente, construído do zero.

## Projetos

### 01 — First Chain
Chain básica com `PromptTemplate` e sintaxe LCEL moderna (`prompt | llm`).
Qualificador de leads B2B que retorna JSON estruturado via Groq/LLaMA.

### 02 — Memory
Conversa com memória entre turnos usando `RunnableWithMessageHistory`.
O modelo lembra contexto de mensagens anteriores na mesma sessão.

## Stack
- LangChain + LangChain Core
- Groq API (llama-3.1-8b-instant)
- Python 3.11+

## Como rodar
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
pip install langchain langchain-groq python-dotenv
```
Crie um `.env` com `GROQ_API_KEY=sua_chave`.
