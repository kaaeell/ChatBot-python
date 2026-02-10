# Simple Chatbot Project

A beginner-friendly chatbot project that's easy to understand and extend.

## Current Features
- Basic greeting responses
- Simple keyword matching
- Conversation history tracking
- Interactive chat session

## How to Run
```bash
python main.py
```

Then just type messages and chat! Type `quit` to exit.

## TODO - Future Tasks

### Day 2: Improve Response Quality
- [ ] Add more diverse responses to the `_load_basic_responses()` method
- [ ] Implement fuzzy string matching (use `difflib` or `fuzzywuzzy` library)
- [ ] Add more greeting variations

### Day 3: Data Persistence
- [ ] Save conversation history to a JSON file
- [ ] Load previous conversations
- [ ] Create a `utils.py` file for helper functions

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
├── README.md        (This file)
├── utils.py         (To be created - helper functions)
├── data/            (To be created - store conversations)
└── requirements.txt (To be created - dependencies)
```

## Notes
- Code is kept simple and readable
- Each method has a clear purpose
- TODO comments show where to enhance
