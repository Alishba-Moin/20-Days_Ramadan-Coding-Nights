import google.generativeai as genai  # Import Google Generative AI
import os  # Import OS module for environment variables
import chainlit as cl  # Import Chainlit for chatbot functionality
from dotenv import load_dotenv  # Import dotenv to load environment variables

# Load environment variables from .env file
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")  # Fetch API key from environment

# Configure Generative AI with the API key
genai.configure(api_key=gemini_api_key)

# Initialize Gemini AI model with a specific version
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Event handler for chat start
@cl.on_chat_start
async def handle_chat_start():
    await cl.Message(content="Hello! How can I assist you today?").send()  # Initial greeting message

# Event handler for handling user messages
@cl.on_message
async def handle_message(message=cl.Message):
    try:
        prompt = message.content  # Extract user input from message
        response = model.generate_content(prompt)  # Generate response using Gemini AI
        response_text = response.text if hasattr(response, "text") else "Sorry, I couldn't process your request."
        
        # Send response back to the user
        await cl.Message(content=response_text).send()
    except Exception as e:
        # Handle any errors and notify the user
        await cl.Message(content=f"An error occurred: {str(e)}").send()
