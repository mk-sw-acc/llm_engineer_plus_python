from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

model = "gpt-5-mini"

# MCP server doesn't work since it is not available anymore, however example code probably is okey
resp = client.responses.create(
    model=model,
    tools=[
        {
            "type": "mcp",
            "server_label": "dmcp",
            "server_description": "A Dungeons and Dragons MCP server to assist with dice rolling.",
            "server_url": "https://dmcp-server.deno.dev/sse",
            "require_approval": "never",
        },
    ],
    input="Roll 2d4+1",
)

print(resp.output_text)