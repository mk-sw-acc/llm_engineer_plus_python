import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)
# Użyjmy modelu, który na pewno obsługuje tools (np. gpt-4o-mini lub gpt-3.5-turbo)
model = "gpt-4o-mini"

# 1️⃣ Definicja narzędzia (zwróć uwagę na strukturę!)
tools = [
    {
        "type": "function",
        "function": {  # <--- Tego brakowało lub było inaczej zagnieżdżone
            "name": "get_weather",
            "description": "Get current temperature for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                },
                "required": ["location"]
            }
        }
    }
]

# 2️⃣ Twoja funkcja (stub)
def get_weather(location: str):
    return {
        "location": location,
        "temperature_c": 20,
        "conditions": "Sunny"
    }

# 3️⃣ Pierwsze wywołanie modelu
messages = [{"role": "user", "content": "What is the weather like in Paris today?"}]

response = client.chat.completions.create( # <--- ZMIANA z client.responses
    model=model,
    messages=messages,
    tools=tools,
)

response_message = response.choices[0].message
tool_calls = response_message.tool_calls

# 4️⃣ Sprawdzenie czy model chce wywołać funkcję
if tool_calls:
    # Dodajemy odpowiedź asystenta do historii (żeby wiedział co sam 'powiedział')
    messages.append(response_message) 

    for tool_call in tool_calls:
        # Tutaj pobieramy argumenty - w standardowym API to jest atrybut .arguments (jako string JSON)
        args = json.loads(tool_call.function.arguments) # <--- ZMIANA: .function.arguments
        
        if tool_call.function.name == "get_weather":
            result = get_weather(**args)
            
            # 5️⃣ Drugie wywołanie – oddajemy wynik funkcji do modelu
            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": "get_weather",
                "content": json.dumps(result)
            })

    # Ostateczna odpowiedź
    final_response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    
    # 6️⃣ Gotowa odpowiedź tekstowa
    print(final_response.choices[0].message.content)

