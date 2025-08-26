# chatbot/agent.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("AGENT_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def generate_response(conversation):
    """
    Generate a response from Gemini.
    conversation: list of (role, message) tuples.
    Only 'user' role is supported.
    """
    # Convert conversation to Gemini-compatible format
    messages = [{"role": "user", "parts": msg} for role, msg in conversation if role == "user"]

    # Call Gemini directly (no system/model roles, no start_chat)
    response = model.generate_content(messages)

    return response.text.strip()
