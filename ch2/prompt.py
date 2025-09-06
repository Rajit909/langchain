
from utils.llm_utils import get_gemini
from langchain_core.messages import HumanMessage, SystemMessage

llm = get_gemini()

# Example 2: Chat style
# messages = [
#     SystemMessage(content="You are a professional software developer"),
#     HumanMessage(content="Give answere in short, Explain langchain")
# ]

# response = llm.invoke(messages)
# print(response.content)


# Example 1 - Message Prompt Templates as Tuples

chatPrompt= ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant that translate {input_language} to {output_language}."),
     ("human","{text}"),
     ("ai":"")
])

print("Chat Prompt: ", chatPrompt)
print("Chat Prompt Input Variables: ", chatPrompt.input_variables)