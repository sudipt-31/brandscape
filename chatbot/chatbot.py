import google.generativeai as genai
import os

genai.configure(api_key=os.environ["AIzaSyCodguYn3dT4BheYfGmt96b1b0omv0zdrk"])

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)