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
        return response.choices[0].text.strip()  # Return the response text
    except Exception as e:
        return f"Error communicating with AI: {e}"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your chatbot. Ask me anything!')

def ai_response(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text  # Get the user input (text message)
    
    
    response = get_ai_response(user_input)

 
    update.message.reply_text(response)


def error(update: Update, context: CallbackContext) -> None:
    print(f"Update {update} caused error {context.error}")

def main() -> None:
    
    updater = Updater("YOUR_BOT_TOKEN")

    dispatcher = updater.dispatcher

    
    dispatcher.add_handler(CommandHandler("start", start))

    
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, ai_response))

    # Add error handler (optional)
    dispatcher.add_error_handler(error)

    
    updater.start_polling()

    
    updater.idle()

if __name__ == '__main__':
    main()
    
