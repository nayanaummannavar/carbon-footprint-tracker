import os
import time
from groq import Groq
from dotenv import load_dotenv

# load environment variables
load_dotenv()

class GroqClient:

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=api_key)

    def generate_response(self, prompt):
        for attempt in range(3):  # retry 3 times
            try:
                response = self.client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                return response.choices[0].message.content

            except Exception as e:
                print(f"Error (attempt {attempt+1}):", e)
                time.sleep(2 ** attempt)  # exponential backoff

        # fallback if all retries fail
        return {
            "error": "AI service unavailable",
            "is_fallback": True
        }