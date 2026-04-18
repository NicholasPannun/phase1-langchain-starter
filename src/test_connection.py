from config.settings import settings
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model=settings.ollama_model,
    base_url=settings.ollama_base_url,
)

response = llm.invoke("Reply with exactly these two words: connection successful")

print(response.content)