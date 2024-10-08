import groq
import os
from fastapi import FastAPI, requests
from dotenv import load_dotenv

load_dotenv()

# set API_Key
GROQ_API_KEY =  os.environ.get("GROQ_API_KEY")
groq_client = groq.Groq(api_key = GROQ_API_KEY)

sys_prompt = """ You an helpful assistance.
                 your goal is to provide useful and relevant response to my request
"""

models = [ "llama-3.1-405b-reasoning",
          "llama-3.1-70b-versatile",
          "llama-3.1-8b-instant",
          "mixtral-8x7b-32768"       
]


def generate( query: str, model: str, temperature = 0):
    response = groq_client.chat.completions.create(
        model = model,
        messages = [{ "role" : "system", "content": sys_prompt},
                    {"role": "user", "content": query}
        ],
        response_format = {"type": "text"},
        temperature = temperature
    )

    answer = response.choices[0].message.content
    return answer

# if __name__ == "__main__":
#     model = models[2]
#     query = "Which is greater, 9.9 or 9.11?"
#     response = generate(query, model, temperature = 1)
#     print(response)
