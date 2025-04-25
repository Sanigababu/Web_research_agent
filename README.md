# 🧠 Web Research Agent

A powerful AI-driven assistant that searches the web, extracts key content, and summarizes it into a concise research report. Powered by Google Gemini, Serper.dev, and Streamlit.The Web Research Agent automates the entire process of online research:
It analyzes a user's question, searches the web, extracts key information from pages, and generates a clean, summarized report — in minutes, with minimal user effort.

---

## 🚀 Live Demo

[🔗 Visit the App](https://YOUR-STREAMLIT-APP-URL)  
_(replace with your actual deployed link)_

---

## 📚 Features

- 🔍 Web search using Serper.dev (Google search API)
- 📄 Text extraction with BeautifulSoup
- 🤖 Smart summarization using Google Gemini Pro 2.5 (March 25 experimental model)
- 📦 Clean markdown report generation
- 💬 Streamlit-based interactive UI
- 🧪 Test script for quick verification

---

## 🧠 Architecture

```plaintext
User Input (Query)
    ↓
Agent Activation → search_web(query)
    ↓
Extracted Links (top 3)
    ↓
extract_text(url) for each page
    ↓
summarize_with_gemini(text, query)
    ↓
Markdown report with sources
    ↓
Streamlit frontend display
```
---

## ⚙️ Tech Stack

- **Frontend:** Streamlit

- **Backend:** Python

- **AI Model:** Google Gemini 2.5 Pro (GenerativeAI)

- **Web Search:** Serper.dev (Google Search API)

- **Web Scraping:** BeautifulSoup4

- **Environment Management:** python-dotenv

- **Deployment:** Streamlit Cloud

## 🧪 Installation
**1.Clone the repo**

```bash
git clone https://github.com/YOUR_USERNAME/web-research-agent.git
cd web-research-agent
```
**2.Install dependencies**

```bash
pip install -r requirements.txt
```

**3.Create a .env file with the following:**

```env
SERPER_API_KEY=your_serper_api_key_here
GEMINI_API_KEY=your_google_api_key_here
```

**4.Run the app locally**

```bash
streamlit run main.py
```

## 🧪 Testing
Run the agent from the command line:

```bash
python test_agent.py
```
Or test specific queries:

```
from agent import run_agent
print(run_agent("what are the effects of climate change on agriculture
```

## 🌐 Deployment
You can deploy easily on:

- **Streamlit Cloud**

### Streamlit Cloud Deployment Steps:

1. Push your project to a GitHub repository.
2. Go to Streamlit Cloud → New App → Connect to GitHub.
3. Set up Secrets (not .env) in App Settings:

```plaintext
SERPER_API_KEY = your-serper-key
GEMINI_API_KEY = your-gemini-key
```
4. Click **"Deploy"**


