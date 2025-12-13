import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

model = "gpt-5-nano"

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "doc.pdf")

file = client.files.create(
    file=open(file_path, "rb"),
    purpose="user_data"
)

response = client.responses.create(
    model=model,
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "file_id": file.id,
                },
                {
                    "type": "input_text",
                    "text": "Summarize the document in 3 sentences. Do this in polish language.",
                },
            ]
        }
    ]
)

print(response.output_text)