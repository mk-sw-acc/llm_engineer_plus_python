import os
from dotenv  import load_dotenv
from openai import OpenAI

model = "gpt-5-nano"

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

response = client.responses.create(
    model=model,
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Analyze the letter and provide a summary of the key points.",
                },
                {
                    "type": "input_file",
                    "file_url": "https://www.berkshirehathaway.com/letters/2024ltr.pdf",
                },
            ],
        },
    ]
)

print(response.output_text)