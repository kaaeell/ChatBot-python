# Simple Chatbot Project

A beginner-friendly chatbot project that's easy to understand and extend.

## Current Features
- Basic greeting responses
- Simple keyword matching
- Conversation history tracking
- Interactive chat session
- Simple learning mode: teach the bot new replies
- More human-style replies with a bit of personality (uses your name in some answers)
- **NEW: Data Persistence** - Conversations and learned responses are now saved!
  - Automatically saves when you quit
  - Loads previous conversations when you restart
  - Remembers all the custom replies you taught it
- **NEW: Separate learned responses** - Custom replies have priority over built-in ones

## How to Run
```bash
python main.py
```

Then give your bot a name, tell it your name, and just type messages and chat! Type `quit` to exit.

### Teaching the Bot New Replies

If the bot doesn't understand something you say, it will respond that it doesn't know how to reply.
You can then teach it:

1. When asked **"Do you want to teach me a reply? (yes/no)"**, type `yes`.
2. Then type the reply you want the bot to use next time you write the same message.

From that point on, the bot will remember and use your custom reply.

## Data Persistence

The bot now automatically saves your conversations! Here's how it works:

- When you type `quit`, the bot saves:
  - Your entire conversation history
  - All custom replies you taught it
  - Your name and the bot's name
  - A timestamp of when the conversation ended

- Next time you run the bot with the same bot name:
  - It loads all previously learned responses
  - Tells you when your last conversation was
  - Continues to learn new responses

All data is saved in the `data/` folder as JSON files (one per bot name).

## TODO - Future Tasks

### Day 2: Improve Response Quality
- [x] Add more diverse responses to the `_load_basic_responses()` method
- [x] Implement fuzzy string matching (use `difflib` or `fuzzywuzzy` library)
- [x] Add more greeting variations

### Day 3: Data Persistence
- [x] Save conversation history to a JSON file
- [x] Load previous conversations
- [x] Create a `utils.py` file for helper functions

### Day 4: Advanced NLP
- [ ] Integrate a real NLP library (spaCy or NLTK)
- [ ] Add sentiment analysis
- [ ] Implement entity recognition

### Day 5: User Profiles
- [ ] Remember user names
- [ ] Store user preferences
- [ ] Personalize responses based on history

### Day 6+: Extra Features
- [ ] Web interface (Flask or Django)
- [ ] Database integration
- [ ] Multi-user support
- [ ] API endpoint

## Project Structure
```
projects365/
├── main.py          (Core chatbot logic)
├── utils.py         (Helper functions for data persistence)
├── README.md        (This file)
├── .gitignore       (Git ignore file)
├── data/            (Auto-created - stores conversation histories)
│   └── *_history.json
└── requirements.txt (To be created - dependencies)
```

## Notes
- Code is kept simple and readable
- Each method has a clear purpose
- TODO comments show where to enhance
