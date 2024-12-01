import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Define a function that gets a response from GPT-3/4.
def get_ai_response(user_input: str) -> str:
    try:
        # Send the input to OpenAI's API and get the model's response
        response = openai.Completion.create(
            model="text-davinci-003",  # or use "gpt-3.5-turbo" or "gpt-4" if available
            prompt=user_input,
            max_tokens=150
        )
        return response.choices[0].text.strip()  # Return the response text
    except Exception as e:
        return f"Error communicating with AI: {e}"

# Define a command handler for the /start command.
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your chatbot. Ask me anything!')

# Define a message handler that will process user messages and send them to the AI.
def ai_response(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text  # Get the user input (text message)
    
    # Get AI's response to the user's message
    response = get_ai_response(user_input)

    # Send the AI response back to the user
    update.message.reply_text(response)

# Error handler (optional)
def error(update: Update, context: CallbackContext) -> None:
    print(f"Update {update} caused error {context.error}")

def main() -> None:
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
    updater = Updater("YOUR_BOT_TOKEN")

    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))

    # Add message handler to process all text messages with AI
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, ai_response))

    # Add error handler (optional)
    dispatcher.add_error_handler(error)

    # Start the bot
    updater.start_polling()

    # Run the bot until you send a signal (e.g., Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
    
