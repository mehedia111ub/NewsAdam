import requests

def generate_news(source_text, topic, word_limit):
    prompt = f"""
You are a professional journalist.
Using the information below, write a news article about: {topic}

Requirements:
- Professional news style
- No repetition
- Maximum {word_limit} words

Sources:
{source_text}
"""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )
    return response.json()["response"]
