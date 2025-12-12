import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("API key not found, exit")
    os.exit(1)

openai = OpenAI(api_key=api_key)
response = openai.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {
            "role": "user", 
            "content": "Tell me a funny joke"
        }
    ]
)
print(json.dumps(response.model_dump(), indent=4))
print(f"\n\nMessage: {response.choices[0].message.content}")