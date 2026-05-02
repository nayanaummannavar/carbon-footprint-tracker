from services.groq_client import GroqClient

client = GroqClient()

response = client.generate_response("Explain carbon footprint in simple terms")

print(response)