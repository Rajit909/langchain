
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from decouple import config


GENAI_API_KEY = config('GEMINI_API_KEY')

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GENAI_API_KEY  
)

# Example 2: Chat style
messages = [
    SystemMessage(content="You are a professional software developer"),
    HumanMessage(content="can you create images?")
]

response = llm.invoke(messages)
print(response)