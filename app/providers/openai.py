from openai import OpenAI
from app.config import OPENAI_API_KEY

if not OPENAI_API_KEY:
    raise RuntimeError("*******************************************OPENAI_API_KEY is not set*******************************************")

client = OpenAI(api_key=OPENAI_API_KEY)

def generate(prompt: str, model: str) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content or ""
