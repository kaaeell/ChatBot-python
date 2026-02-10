class SimpleBot:
    def __init__(self, name):
        self.name = name
        self.responses = {
            "hello": "Hi!",
            "hi": "Hey!",
            "how are you": "Good!",
            "bye": "Goodbye!",
        }
        self.history = []
    
    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        if user_input in self.responses:
            return self.responses[user_input]
        
        for keyword in self.responses:
            if keyword in user_input:
                return self.responses[keyword]
        
        return "Tell me more."
    
    def chat(self):
        print(f"\n{self.name}: Hello! I'm {self.name}. Type 'quit' to exit.\n")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() == "quit":
                print(f"{self.name}: Goodbye!")
                break
            
            response = self.get_response(user_input)
            print(f"{self.name}: {response}\n")
            self.history.append((user_input, response))


bot_name = input("What's your bot's name? ")
bot = SimpleBot(bot_name)
bot.chat()
