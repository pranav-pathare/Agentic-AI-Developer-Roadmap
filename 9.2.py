from google import genai

client = genai.Client(api_key="AQ.Ab8RN6IcqeOVjX19LpLutLXCxd3Xnf7h1kegAlUORnnzL9sv1g")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hello"
)
print(interaction.output_text)