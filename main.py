import random
import difflib


class SimpleBot:
    def __init__(self, name, user_name=None):
        self.name = name
        self.user_name = user_name

        self.responses = self._load_basic_responses()
        self.history = []

    def _load_basic_responses(self):
        """Return a basic set of patterns and replies."""
        responses = {
            "hello": [
                "Hi {user}!",
                "Hey there!",
                "Hello :)",
                "Nice to see you, {user}.",
                "Oh hey, {user}!",
            ],
            "hi": [
                "Hey!",
                "Hi {user}!",
                "Yo :)",
                "Hi there.",
            ],
            "how are you": [
                "I'm doing good, thanks for asking!",
                "Pretty good today. How about you, {user}?",
                "I'm just a simple bot, but I'm happy to chat.",
                "Can't complain. How's your day going?",
            ],
            "bye": [
                "Goodbye {user}, talk soon!",
                "See you later!",
                "Bye!",
                "Take care, {user}.",
            ],
        }
        return responses

    def _personalize(self, text):
        if "{user}" in text:
            if self.user_name:
                return text.replace("{user}", self.user_name)
            return text.replace("{user}", "there")
        return text
    
    def get_response(self, user_input):
        user_input = user_input.lower().strip()


        if user_input in self.responses:
            return self._personalize(random.choice(self.responses[user_input]))

        for keyword in self.responses:
            if keyword in user_input:
                return self._personalize(random.choice(self.responses[keyword]))

        close = difflib.get_close_matches(user_input, self.responses.keys(), n=1, cutoff=0.6)
        if close:
            key = close[0]
            return self._personalize(random.choice(self.responses[key]))

        return None
    
    def chat(self):
        if self.user_name:
            print(f"\n{self.name}: Hey {self.user_name}, I'm {self.name}. Type 'quit' to exit.\n")
        else:
            print(f"\n{self.name}: Hello! I'm {self.name}. Type 'quit' to exit.\n")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() == "quit":
                print(f"{self.name}: Goodbye!")
                break
            
            response = self.get_response(user_input)

            if response is None:
                print(f"{self.name}: I don't know how to respond to that.")
                teach = input(f"{self.name}: Do you want to teach me a reply? (yes/no) ").strip().lower()
                if teach in ("yes", "y"):
                    new_reply = input(f"{self.name}: What should I say next time? ").strip()
                    if new_reply:
                        normalized = user_input.lower().strip()
                        self.responses[normalized] = new_reply
                        response = new_reply
                        print(f"{self.name}: Got it, I'll remember that!\n")
                    else:
                        response = "Okay, maybe next time."
                else:
                    response = "Okay, let's talk about something else."

            print(f"{self.name}: {response}\n")
            self.history.append((user_input, response))


bot_name = input("What's your bot's name? ")
user_name = input("And what's your name? ")
user_name = user_name.strip() or None
bot = SimpleBot(bot_name, user_name=user_name)
bot.chat()
