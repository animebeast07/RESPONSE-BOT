import re, os, time
id_pattern = re.compile(r'^.\d+$') 
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "26169469")
    API_HASH  = os.environ.get("API_HASH", "1e2225f3d65b401d7d5bb921af531712")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7734830076:AAGP4pqZC1nR1Q3NecBu8O-tG1EGYO-lBfI") 
    import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

def get_ai_response(user_input: str) -> str:
    try:
        
        response = openai.Completion.create(
            model="text-davinci-003",  # or use "gpt-3.5-turbo" or "gpt-4" if available
            prompt=user_input,
            max_tokens=150
        )
        return response.choices[0].text.strip()  # Return the res
