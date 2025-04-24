from search_tool import search_web
from scraper import extract_text
from summarizer import summarize_with_gemini

def run_agent(query):
    print("👉 [agent.py] Received query:", query)
    results = search_web(query)
    print("🔎 [agent.py] Search results:", results)
    report = ""

    for title, url in results:
        print(f" Scraping: {title} - {url}")
        text = extract_text(url)
        if "Error" not in text and text.strip():
            summary = summarize_with_gemini(text, query,url)
            report += f" {title}\n🔗 {url}\n📝 {summary}\n\n"
        else:
            print("⚠️ Skipping URL due to extraction error or empty content.")
    return report if report.strip() else "No useful content could be retrieved. Try a different question."
