import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_llm(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": 'llama3',
            "prompt": prompt,
            "stream": False
        },
        timeout=600
    )
    return response.json()["response"]









# import os
# from dotenv import load_dotenv
# from openai import OpenAI


# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def ask_llm(prompt):
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.4
#     )
    
#     return response.choices[0].message.content

