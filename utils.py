import json
import os
from datetime import datetime


def save_conversation_history(bot_name, user_name, history, learned_responses):
    """Save conversation history and learned responses to a JSON file."""
    if not os.path.exists("data"):
        os.makedirs("data")
    
    filename = f"data/{bot_name.lower().replace(' ', '_')}_history.json"
    
    data = {
        "bot_name": bot_name,
        "user_name": user_name,
        "timestamp": datetime.now().isoformat(),
        "history": history,
        "learned_responses": learned_responses
    }
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving history: {e}")
        return False


def load_conversation_history(bot_name):
    """Load conversation history and learned responses from a JSON file."""
    filename = f"data/{bot_name.lower().replace(' ', '_')}_history.json"
    
    if not os.path.exists(filename):
        return None
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error loading history: {e}")
        return None


def list_saved_bots():
    """List all saved bot conversations."""
    if not os.path.exists("data"):
        return []
    
    bot_files = [f for f in os.listdir("data") if f.endswith("_history.json")]
    bots = [f.replace("_history.json", "").replace("_", " ").title() for f in bot_files]
    return bots


def format_timestamp(iso_string):
    """Format an ISO timestamp into a readable string."""
    try:
        dt = datetime.fromisoformat(iso_string)
        return dt.strftime("%Y-%m-%d %I:%M %p")
    except:
        return iso_string
