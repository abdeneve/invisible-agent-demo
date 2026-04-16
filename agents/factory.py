from langchain_openai import ChatOpenAI
from config.settings import settings

def get_model() -> ChatOpenAI:
    """Retorna uma instância configurada do modelo OpenAI."""
    return ChatOpenAI(
        api_key=settings.openai_api_key,
        model=settings.llm_model,
        temperature=0
    )
