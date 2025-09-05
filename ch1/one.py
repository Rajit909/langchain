
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from decouple import config


GENAI_API_KEY = config('GEMINI_API_KEY')

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=GENAI_API_KEY  
)

# Example 1: Simple text query
response = llm.invoke("Who is the Prime Minister of India?")
print(response)

# Example 2: Chat style
messages = [
    SystemMessage(content="You are a standup comedian"),
    HumanMessage(content="Tell me a joke about programmers")
]

response = llm.invoke(messages)
print(response)
