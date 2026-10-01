from google import genai

client = genai.Client()

automatically

interaction = client.interactions.create( model="gemini-2.5-flash", input="Explain neural networks to a beginner, " "using one everyday analogy."

print (interaction.output text)