from decouple import config
from langchain_google_genai import ChatGoogleGenerativeAI

def get_gemini(model_name: str = "gemini-2.5-flash") -> ChatGoogleGenerativeAI:
    """
    Returns a reusable Gemini model instance.
    Reads the GEMINI_API_KEY from .env using python-decouple.
    """
    api_key = config("GEMINI_API_KEY", default=None)
    if not api_key:
        raise ValueError("❌ GEMINI_API_KEY not found in environment. Check your .env file.")

    return ChatGoogleGenerativeAI(
        model=model_name,
        google_api_key=api_key
    )
