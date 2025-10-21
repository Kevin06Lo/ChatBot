from openai import OpenAI
from dotenv import load_dotenv
import os

#Load .env file variables
load_dotenv()

#Initialize client using my key from .env
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def ai_response(prompt):
    try:
        completion = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a friendly and helpful chatbot"},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"