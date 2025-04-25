from search_tool import search_web
from scraper import extract_text
from summarizer import summarize_with_gemini

def run_agent(query):
    log = []  # Reasoning log
    report = f"# 🧠 Answer to: **{query}**\n\n"
    
    log.append(f"📩 Received query: '{query}'")
    log.append("🔍 Performing web search...")

    results = search_web(query)
    log.append(f"🔗 Found {len(results)} results.")

    if not results:
        log.append("❌ No results found. Stopping.")
        return "\n".join(log) + "\n\nNo useful results found."

    for idx, (title, url) in enumerate(results, 1):
        log.append(f"\n---\n🔸 Result {idx}: {title} ({url})")
        log.append("→ Attempting to extract content...")
        text = extract_text(url)

        if "Error" not in text and text.strip():
            log.append("✅ Content extracted successfully.")
            log.append("→ Summarizing content using Gemini...")
            summary = summarize_with_gemini(text, query, url)
            log.append("✅ Summary generated.")

            report += f"## {idx}. {title}\n"
            report += f"[🔗 Source]({url})\n\n"
            report += f"**Summary:**\n{summary.strip()}\n\n"
        else:
            log.append("⚠️ Skipping — extraction failed or content empty.")

    if "##" not in report:
        log.append("⚠️ No valid content was found from any sources.")
        return "\n".join(log) + "\n\nNo useful content could be retrieved."

    log.append("\n✅ Finished processing all results.")
    return "\n".join(log) + "\n\n---\n\n" + report

