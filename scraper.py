import requests
from bs4 import BeautifulSoup

def extract_text(url):
    try:
        res=requests.get(url,timeout=5)
        soup=BeautifulSoup(res.content,'html.parser')
        paragraphs=soup.find_all('p')
        return " ".join(p.get_text() for p in paragraphs[:10]) #limit to avoid overload
    except Exception as e:
        return f"Error: {e}"

        