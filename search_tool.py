import requests
import os
from dotenv import load_dotenv
load_dotenv()

def search_web(query):
    url = "https://google.serper.dev/search"
    headers={
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json"
    }
    payload={"q":query}
    response = requests.post(url, headers=headers, json=payload)
    results = response.json().get("organic",[])
    return [(item["title"],item["link"]) for item in results[:3]]