import random
import difflib
import utils


class SimpleBot:
    def __init__(self, name, user_name=None):
        self.name = name
        self.user_name = user_name

        self.responses = self._load_basic_responses()
        self.learned_responses = {}  # Track custom learned responses separately
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
    
    def load_previous_data(self):
        """Load previous conversation history and learned responses."""
        data = utils.load_conversation_history(self.name)
        if data:
            self.learned_responses = data.get("learned_responses", {})
            old_history = data.get("history", [])
            if old_history:
                print(f"\n{self.name}: I found our previous conversation from {utils.format_timestamp(data['timestamp'])}!")
                print(f"{self.name}: We had {len(old_history)} messages before.\n")
            return True
        return False
    
    def save_data(self):
        """Save conversation history and learned responses."""
        return utils.save_conversation_history(
            self.name, 
            self.user_name, 
            self.history,
            self.learned_responses
        )
    
    def get_response(self, user_input):
        user_input = user_input.lower().strip()

        # Check learned responses first (higher priority)
        if user_input in self.learned_responses:
            return self._personalize(random.choice(self.learned_responses[user_input]))

        # Then check built-in responses
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
        # Load previous data if available
        self.load_previous_data()
        
        if self.user_name:
            print(f"\n{self.name}: Hey {self.user_name}, I'm {self.name}. Type 'quit' to exit.\n")
        else:
            print(f"\n{self.name}: Hello! I'm {self.name}. Type 'quit' to exit.\n")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() == "quit":
                print(f"{self.name}: Saving our conversation...")
                if self.save_data():
                    print(f"{self.name}: Saved! See you next time!")
                else:
                    print(f"{self.name}: Couldn't save, but goodbye anyway!")
                break
            
            response = self.get_response(user_input)

            if response is None:
                print(f"{self.name}: I don't know how to respond to that.")
                teach = input(f"{self.name}: Do you want to teach me a reply? (yes/no) ").strip().lower()
                if teach in ("yes", "y"):
                    new_reply = input(f"{self.name}: What should I say next time? ").strip()
                    if new_reply:
                        normalized = user_input.lower().strip()
                        if normalized in self.learned_responses:
                            self.learned_responses[normalized].append(new_reply)
                        else:
                            self.learned_responses[normalized] = [new_reply]
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
