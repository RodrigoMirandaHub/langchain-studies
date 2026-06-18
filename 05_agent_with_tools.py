import csv
csv.field_size_limit(10_000_000)

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from ddgs import DDGS

load_dotenv()

llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0)

@tool
def calculator(expression: str) -> str:
    """Avalia uma expressão matemática simples, ex: '23 * 4 + 10'."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Erro ao calcular: {e}"


@tool
def buscar_na_internet(query: str) -> str:
    """Busca informações atuais na internet sobre um tópico."""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
        if not results:
            return "Nenhum resultado encontrado."
        return "\n".join([r["body"] for r in results])
    except Exception as e:
        return f"Erro na busca: {e}"


tools = [calculator, buscar_na_internet]
tools_map = {t.name: t for t in tools}

llm_with_tools = llm.bind_tools(tools)


def ask(question):
    print(f"\nPergunta: {question}")
    messages = [HumanMessage(content=question)]

    response = llm_with_tools.invoke(messages)
    messages.append(response)

    # Se o modelo chamou uma tool
    while response.tool_calls:
        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]
            print(f"  → Usando tool: {tool_name}({tool_args})")

            tool_result = tools_map[tool_name].invoke(tool_args)

            messages.append(ToolMessage(
                content=str(tool_result),
                tool_call_id=tool_call["id"]
            ))

        response = llm_with_tools.invoke(messages)
        messages.append(response)

    print(f"Resposta: {response.content}")


ask("Quanto é 347 * 12 + 89?")
ask("Quem é o presidente atual do Brasil?")
ask("Qual é a capital da França?")