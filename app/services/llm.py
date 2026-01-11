# import requests

# OLLAMA_URL = "http://localhost:11434/api/generate"


# def ask_llm(prompt):
#     response = requests.post(
#         OLLAMA_URL,
#         json={
#             "model": 'llama3',
#             "prompt": prompt,
#             "stream": False
#         },
#         timeout=600
#     )
#     return response.json()["response"]


from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "You are an expert technical recruiter."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=1024
    )

    return response.choices[0].message.content



 



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

