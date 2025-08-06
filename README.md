# 🤖 Telegram AI Bot - "Echo"

An intelligent Telegram bot that uses [LangChain](https://www.langchain.com/), [Groq](https://groq.com/), [LangGraph](https://github.com/langchain-ai/langgraph), and [Tavily](https://www.tavily.com/) to respond to messages effectively and step-by-step.

---

## 🚀 Features

- Uses **Groq + LLaMA 3.3-70B** as the LLM.
- Acts as an assistant called *Echo*, designed to be **concise, helpful, and always think step-by-step**.
- Can perform **web searches** thanks to Tavily.
- Direct interaction via the **Telegram Bot API**.
- Built with **LangChain + LangGraph**.

---

## 📦 Requirements

- Python 3.10+
- A Groq API key
- A Tavily API key (optional, but recommended)
- A Telegram Bot (created via [@BotFather](https://t.me/BotFather))

---

## 🛠️ Installation

1. **Clone the project**

```bash
git clone https://github.com/ldcostanzo/Bot-Telegram-AI.git
cd Bot-Telegram-AI
```
2. **Create a virtual environment in VS Code**
Linux
```bash
python -m venv venv
source venv/bin/activate
```
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

3.**Install dependencies**
```bash
pip install -r requirements.txt

```
4.**Rename the .env_example file to .env**
```bash
BOT_TOKEN=your_telegram_bot_token
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key  # optional, if using TavilySearchResults

```
5. **Run the bot**
```bash
python main.py

```
