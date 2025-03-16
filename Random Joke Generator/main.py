import streamlit as st
import requests

# Custom CSS for a more professional look
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f8f9fa;
    }
    .subtitle {
        color: #6c757d;
        text-align: center;
        margin-bottom: 20px;
    }
    .joke-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
        color: #333333;
    }
    .footer {
        text-align: center;
        color: #888888;
        margin-top: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def generate_random_joke():
    '''Fetch a random joke from the API'''
    try:
        response = requests.get("https://randomjokefastapi.vercel.app/jokes")

        if response.status_code == 200:
            joke_data = response.json()

            # Extract joke from JSON response
            if "Jokes" in joke_data:
                return f"{joke_data['Jokes']['setup']} \n\n {joke_data['Jokes']['punchline']}"
            else:
                return "Oops! The joke database seems to be shy today. Try again later!"
        else:
            return f"Unexpected API response: {response.status_code}"

    except Exception as e:
        return f"Oops! Something went wrong. Error: {str(e)}"

def main():
    st.title("😂 Random Joke Generator")
    st.markdown("<p class='subtitle'>Click the button below to hear a joke that will make your day!</p>", unsafe_allow_html=True)

    if st.button("Tell Me a Joke 🎭"):
        joke = generate_random_joke()
        st.markdown(f"<div class='joke-box'>{joke}</div>", unsafe_allow_html=True)

    st.markdown("<div class='footer'>Powered by <b>Joke API</b> | Created with ❤️ by <a href='https://github.com/alishba-moin'>Alishba Moin</a></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
