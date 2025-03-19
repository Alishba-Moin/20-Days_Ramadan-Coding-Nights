import chainlit as cl  # Importing the Chainlit library


# This function runs when a new message is received
@cl.on_message
async def main(message: cl.Message):

    # Creating a response by echoing the user's input
    response = f"You said: {message.content}"

    # Sending the response back to the user
    await cl.Message(content=response).send()
