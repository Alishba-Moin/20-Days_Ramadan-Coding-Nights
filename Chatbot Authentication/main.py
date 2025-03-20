import os  # Importing the OS module to set environment variables
import google.generativeai as genai  # Importing Google's Generative AI module
import chainlit as cl  # Importing Chainlit for chatbot interaction
from dotenv import load_dotenv  # Importing dotenv to load environment variables from .env file
from typing import Optional, Dict  # Importing types for type hinting

# Load environment variables from the .env file
load_dotenv()

# Get the API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Configure the generative AI model with the API key
genai.configure(api_key=gemini_api_key)

# Initialize the generative model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# OAuth Callback Function: Handles authentication from GitHub or Google
@cl.oauth_callback
def oauth_callback(
    provider_id: str,
    token: str,
    raw_user_data: Dict[str, str],
    default_user: cl.User
) -> Optional[cl.User]:
    """
    Handles the OAuth callback from GitHub.
    Returns the authenticated user if successful.
    """

    print(f"Provider: {provider_id}")  # Print the provider name (e.g., GitHub or Google)
    print(f"User Data: {raw_user_data}")  # Print user details from authentication

    return default_user  # Return the authenticated user

# Function to handle when the chat starts
@cl.on_chat_start
async def handle_chat():
    """
    This function runs when the chat starts.
    It initializes an empty chat history and sends a welcome message.
    """

    cl.user_session.set("history", [])  # Initialize empty chat history

    await cl.Message(content="Hello! How can I assist you today?").send()  # Send welcome message

# Function to handle incoming user messages
@cl.on_message
async def handle_message(message: cl.Message):
    """
    This function is triggered when a user sends a message.
    It processes the user's message, generates a response, and updates the chat history.
    """

    # Retrieve chat history from the session
    history = cl.user_session.get("history")

    # Add the user's message to chat history
    history.append({"role": "user", "content": message.content})

    # Format chat history for AI model
    formatted_history = []

    for msg in history:
        role = "user" if msg["role"] == "user" else "model"

        formatted_history.append({"role": role, "parts": [{"text": msg["content"]}]})

    # Generate response using the AI model
    response = model.generate_content(formatted_history)

    # Extract response text (handling possible errors)
    response_text = response.text if hasattr(response, "text") else "Sorry, I couldn't process your request."

    # Add the AI's response to chat history
    history.append({"role": "assistant", "content": response_text})

    # Save updated history to the session
    cl.user_session.set("history", history)

    # Send the response to the user
    await cl.Message(content=response_text).send()
