from openai import OpenAI
from decouple import config
from langchain_openai import ChatOpenAI
OPENAI_API_KEY = config('OPENAI_API_KEY')

client = OpenAI(
  api_key=SECRET_KEY
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message)
