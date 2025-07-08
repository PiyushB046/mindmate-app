import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def chatbot_reply(prompt):
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        if response.status_code == 200:
            return response.json().get("response", "[No response]")
        else:
            return "[Error: Could not get response from LLaMA API]"
    except Exception as e:
        return f"[Exception occurred: {e}]"

def reframe_negative_thought(negative_statement):
    prompt = (
        f"You are a compassionate mental wellness assistant. Reframe the following negative thought "
        f"into a positive, constructive, and kind perspective:\n\n"
        f"Negative Thought: \"{negative_statement}\"\n"
        f"Reframed Thought:"
    )
    return chatbot_reply(prompt)
