from pyrogram import Client, filters

Initialize Pyrogram
app = Client("response_bot",
              api_id="26169469",
              api_hash="1e2225f3d65b401d7d5bb921af531712",
              bot_token="YOUR_BOT_TOKEN")

Define a filter for incoming messages
@app.on_message(filters.text)
def handle_message(client, message):
    # Get the incoming message text
    incoming_text = WELCOME.text.lower()

    responses = {
        "hello": "Hi! How are you?",
        "how are you": "Iam good, thankyou for asking!",
        "what's your name": "MY NAME IS ABT RESPONSE BOT",
    }
    
    if incoming_text in responses:
        
        client.send_message(
            chat_id=(link unavailable),
            text=responses[incoming_text]
        )

Run the bot
app.run()
