from pyrogram import Client, filters

Initialize Pyrogram
app = Client("response_bot",
              api_id="YOUR_API_ID",
              api_hash="YOUR_API_HASH",
              bot_token="YOUR_BOT_TOKEN")

Define a filter for incoming messages
@app.on_message(filters.text)
def handle_message(client, message):
    # Get the incoming message text
    incoming_text = message.text.lower()

    responses = {
        "hello": "Hi! How are you?",
        "how are you": "I'm good, thanks!",
        "what's your name": "My name is Response Bot",
    }

    # Check if the incoming message matches a response
    if incoming_text in responses:
        # Send the response back to the user
        client.send_message(
            chat_id=(link unavailable),
            text=responses[incoming_text]
        )

Run the bot
app.run()
