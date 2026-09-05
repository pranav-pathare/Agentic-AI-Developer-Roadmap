import os
from google import genai

# Read the key from an environment variable (never hardcode secrets in code).
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello"
)
print(response.text)

