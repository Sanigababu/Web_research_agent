import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-2.5-pro-exp-03-25")

def summarize_with_gemini(text, query,url=""):
    if "youtube.com" in url.lower():
        print("⚠️ Skipping YouTube URL.")
    response = model.generate_content(f"Summarize this content in the context of '{query}':\n\n{text}")
    return response.text

    
    

    


