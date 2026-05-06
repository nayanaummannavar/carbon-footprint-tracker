from groq import Groq
import os
from dotenv import load_dotenv

# Load .env HERE (important)
load_dotenv()

def generate_response(prompt):
    try:
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            return "Error: GROQ_API_KEY not found. Check your .env file."

        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"