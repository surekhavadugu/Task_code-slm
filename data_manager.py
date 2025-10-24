import json
import os

MEMORY_FILE = "data/memory.json"

# Ensure the folder exists
os.makedirs("data", exist_ok=True)

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def store_in_memory(question, answer):
    memory = load_memory()
    memory[question] = answer
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)