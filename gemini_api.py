import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key
API_KEY = os.getenv("GEMINI_API_KEY")

# ✅ Debug print to confirm .env loaded
print("🔑 API Key loaded:", bool(API_KEY))

# Raise error if not found
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file. Please check your .env file.")

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)

# Use supported model
MODEL_NAME = "gemini-2.0-flash"

def get_gemini_answer(question):
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=question,
            config=types.GenerateContentConfig(temperature=0)
        )
        return response.text.strip()
    except Exception as e:
        # Handle common Gemini errors gracefully
        if "503" in str(e):
            return "Gemini servers are busy right now 😕. Please try again in a moment."
        elif "API key" in str(e):
            return "API key error — please check your .env file!"
        else:
            return f"Gemini API error: {e}"
