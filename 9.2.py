from google import genai

client = genai.Client(api_key="REMOVED_API_KEY")

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Hello"
)
print(interaction.output_text)