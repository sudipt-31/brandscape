import google.generativeai as genai
import os
os.environ['API_KEY'] = "AIzaSyCodguYn3dT4BheYfGmt96b1b0omv0zdrk"
genai.configure(api_key= os.environ['API_KEY'])

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)