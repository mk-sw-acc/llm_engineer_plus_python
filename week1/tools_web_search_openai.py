import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

model = "gpt-5-nano"

response = client.responses.create(
    model=model,
    tools=[{"type": "web_search"}],
    input="Summary in one sentence a positive latest news story from today in Poland? Don't ask additional questions. Just return the summary."
)

print(response.output_text)