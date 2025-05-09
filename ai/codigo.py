from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

chave_api = os.getenv("OPENAI_API_KEY")

mensagens = [
    SystemMessage("Traduza o texto para inglês"),
    HumanMessage("Inscreva-se no canal.")
]

modelo = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()
chain = modelo | parser

template_mensagem = ChatPromptTemplate.from_messages([
    SystemMessage("Traduza o texto a seguir para {idioma}"),
    HumanMessage("{texto}")
])

print(template_mensagem.invoke({"idioma": "frances", "texto": "Dê like no vídeo"}))

chain = template_mensagem | modelo | parser

texto = chain.invoke({"idioma": "frances", "texto": "Dê like no vídeo"})
print(texto)