import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
import langchain
langchain.verbose = False
langchain.debug =   False
langchain.llm_cache = False
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent

load_dotenv()

def get_ai_response(user_message: str) -> str:
    """Usa LangChain con Groq per generare una risposta."""
    groq_api_key = os.getenv("GROQ_API_KEY")

    if not groq_api_key:
        return "Chiave API Groq mancante."

    # Choose the LLM that will drive the agent
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.1,
    )

    tools = [TavilySearchResults(max_results=3)]
    prompt = "ciao, sei echo, un aiutante che risponde sempre in maniera efficace e sintetica,ragiona sempre step by step"
    agent_executor = create_react_agent(llm, tools, prompt=prompt)

    messages = agent_executor.invoke({"messages": [("user", user_message)]})
    return messages['messages'][-1].content








# inizio

# from typing import Final
# from telegram import Update
# from telegram.ext import Application, ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
# import requests
# import os
# from dotenv import load_dotenv
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_ollama import ChatOllama


# load_dotenv()
# TOKEN :Final = os.getenv("BOT_TOKEN")

# OLLAMA_API_URL = 'http://localhost:11434/api/generate'

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Ciao! Mandami una domanda e ti rispondo con LLaMA 3!")

# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_input = update.message.text

#     response = requests.post(OLLAMA_API_URL, json={
#         "model": "llama3.2:1b",
#         "prompt": user_input,
#         "stream": False
#     })

#     if response.ok:
#         answer = response.json()["response"]
#         await update.message.reply_text(answer)
#     else:
#         await update.message.reply_text("Errore nella richiesta a LLaMA 3.")

# if __name__ == '__main__':
#     app = ApplicationBuilder().token(TOKEN).build()

#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

#     app.run_polling()


#fine


















# from typing import Final
# from telegram import Update
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
# import os
# from dotenv import load_dotenv
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_ollama import ChatOllama


# # Caricamento variabili ambiente
# load_dotenv()
# TOKEN: Final = os.getenv("BOT_TOKEN")
# BOT_USERNAME: Final = os.getenv('BOT_USER')
# URL = os.getenv("URL")

# #instantiate our model object
# llm = ChatOllama(
# model="llama3.2:1b",
#     temperature=0,
#     # other params...
# )


# async def start_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('Hello i\'m your test bot')

# async def help_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('Mi scoccio di scrivere l help ')

# async def custom_command(update: Update,context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('Inserisci il comando custom')

# messages = [
#     (
#         "system",
#         "You are a helpful assistant that translates English to French. Translate the user sentence.",
#     ),
#     ("human", "I love programming."),
# ]
# #generate chat completions
# # ai_msg = llm.invoke(messages)

# # print(ai_msg.content)


# #We can chain our model with a prompt template like so:
# def handle_response(text: str) -> str:
#     messages=[
#             (
#                 "system",
#                 "You are a helpful assistant that translates {input_language} to {output_language}.",
#             ),
#             ("human", "{input}"),
#         ]

#     prompt = ChatPromptTemplate.from_messages(
#         messages=messages
#     )


#     chain = prompt | llm

# def handle_response(text: str) -> str:
#     processed: str = text.lower()

#     if 'ciao' in processed:
#         return 'ciao'

#     if 'come stai' in processed:py
#         return 'bene grazie, tu?'

#     return 'Bro'

# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     message_type: str = update.message.chat.type
#     text: str = update.message.text

#     print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

#     if message_type == 'group' or message_type == 'supergroup':
#         if BOT_USERNAME in text:
#             new_text: str = text.replace(BOT_USERNAME,'').strip()
#             response: str = handle_response(new_text)
#         else:
#             return
#     else:
#         response: str = handle_response(text)
#     print('Bot',response)
#     await update.message.reply_text(response)

# async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     print(f'Update {update} caused error {context.error}')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# if __name__ == '__main__':
#     print('Start bot')
#     app =  Application.builder().token(TOKEN).build()

#     app.add_handler(CommandHandler('start',start_command))
#     app.add_handler(CommandHandler('help',help_command))
#     app.add_handler(CommandHandler('custom',custom_command))

#     app.add_handler(MessageHandler(filters.TEXT,handle_message))

#     app.add_error_handler(error)
    
#     print('Start Polling')
#     app.run_polling(poll_interval=3)

#  Avvia il bot in modalità webhook

#    app.run_webhook(
#         listen="0.0.0.0",
#         port=443,
#         url_path=TOKEN,  # URL locale del webhook
#         webhook_url=f"{URL}/{TOKEN}",  # URL pubblico del webhook
#         key="/certs/key.pem",
#         cert="/certs/cert.pem"
#         )  
# print(f"Webhook configurato su: {URL}/{TOKEN}")
