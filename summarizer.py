import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-2.5-pro-exp-03-25")

def summarize_with_gemini(text, query,url=""):
    if "youtube.com" in url.lower():
        print("⚠️ Skipping YouTube URL.")
    prompt=f"""
    Summarize the following content in relation to research question:'{query}'.
    Focus on relevant facts, explanations, and useful details. Eliminate fluff.
    
    Content:
    {text}
    """
    response = model.generate_content(prompt)
    return response.text

    
    

    


