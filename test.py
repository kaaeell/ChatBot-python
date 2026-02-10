from main import SimpleBot


test_inputs = [
    "hello",
    "Hi",
    "how are you",
    "what's your name?",
    "bye",
    "random message",
]

bot = SimpleBot("TestBot")

for user_input in test_inputs:
    response = bot.get_response(user_input)
    print(f"You: {user_input}")
    print(f"Bot: {response}\n")
    bot.save_message(user_input, response)
