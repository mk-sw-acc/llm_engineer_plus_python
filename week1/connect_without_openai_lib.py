import os
from dotenv import load_dotenv
import requests
import json

load_dotenv(override=True) # load .env file under the hood , override entry every time even if exists
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("API key not found, exit")
    os.exit(1)

headers = {
    "Authorization" : f"Bearer {api_key}"
}

url = "https://api.openai.com/v1/chat/completions"

payload_json = {
    "model": "gpt-5-nano",
    "messages": [
        {
            "role": "user",
            "content": "Tell me a funny joke"
        }
    ]
}

response = requests.post(
    url = url,
    headers = headers,
    json = payload_json
)

print(json.dumps(response.json(), indent=4))

response_msg = response.json()["choices"][0]["message"]["content"]
print(f"\n\Message: {response_msg}")