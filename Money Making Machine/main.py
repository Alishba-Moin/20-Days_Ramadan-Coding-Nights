import streamlit as st
import random
import time
import requests
from streamlit_extras.add_vertical_space import add_vertical_space

# Set page config
st.set_page_config(page_title="Money Making Machine", page_icon="💰", layout="wide")

# Custom styles
st.markdown(
    """
    <style>
        .money-text { font-size: 24px; font-weight: bold; color: #FFD700; }
        .center { text-align: center; }
        .stButton button { background-color: #28a745; color: white; padding: 10px; font-size: 16px; }
        .stButton button:hover { background-color:rgb(96, 167, 111) color: gray; }
        .stTextInput>div>div>input { border-radius: 10px; }
        .stAlert { background-color: #1e1e1e; padding: 10px; border-radius: 10px; color: white; }
        .leaderboard-container { display: flex; align-items: center; gap: 20px; }
        .leaderboard-text { font-size: 20px; color: white; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.title("📍 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Side Hustles", "Money Quotes", "Leaderboard", "Investment Tips"])

# Money Generator 
def generate_money():
    return random.randint(1, 1000)

# API Fetch Functions
def fetch_side_hustles():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles?api_key=1234567890&count=1")
        if response.status_code == 200:
            hustles = response.json()  
            return hustles["side_hustles"]  
        else:
            return "Freelancing"  
    except:
        return "Something went wrong!"

def fetch_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes?api_key=1234567890&count=1")
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quotes"]
        else:
            return "Money is not everything!"
    except:
        return "Something went wrong!"

# Leaderboard Data
leaderboard = [
    {"name": "Alice", "earnings": 500, "image": "https://randomuser.me/api/portraits/women/1.jpg"},
    {"name": "Bob", "earnings": 1200, "image": "https://randomuser.me/api/portraits/men/2.jpg"},
    {"name": "Charlie", "earnings": 800, "image": "https://randomuser.me/api/portraits/men/3.jpg"},
    {"name": "David", "earnings": 1500, "image": "https://randomuser.me/api/portraits/men/4.jpg"},
    {"name": "Eve", "earnings": 1100, "image": "https://randomuser.me/api/portraits/women/5.jpg"},
    {"name": "Frank", "earnings": 950, "image": "https://randomuser.me/api/portraits/men/6.jpg"},
    {"name": "Grace", "earnings": 1750, "image": "https://randomuser.me/api/portraits/women/7.jpg"},
    {"name": "Hannah", "earnings": 600, "image": "https://randomuser.me/api/portraits/women/8.jpg"},
    {"name": "Isaac", "earnings": 1300, "image": "https://randomuser.me/api/portraits/men/9.jpg"},
    {"name": "Jack", "earnings": 700, "image": "https://randomuser.me/api/portraits/men/10.jpg"},
]
sorted_leaderboard = sorted(leaderboard, key=lambda x: x["earnings"], reverse=True)

# Home Page
if page == "Home":
    st.title("💸 Money Making Machine! 💰")
    st.write("Turn your ideas into income!")

    st.subheader("💵 Instant Money Generator")
    if st.button("Generate Money 💰"):
        st.write("⏳ Counting your money...")
        time.sleep(4)
        amount = generate_money()
        st.success(f"🎉 You made **${amount}**")

# Side Hustles Page
elif page == "Side Hustles":
    st.title("🚀 Side Hustle Ideas")
    if st.button("Get a Side Hustle Idea 💼"):
        idea = fetch_side_hustles()
        st.success(f"💡 {idea}")

# Money Quotes Page
elif page == "Money Quotes":
    st.title("💬 Money Quotes")
    if st.button("Inspire Me 💡"):
        quote = fetch_money_quotes()
        st.info(f"📢 {quote}")

# Leaderboard Page
elif page == "Leaderboard":
    st.title("🏆 **Top Earners Leaderboard** 🏆")

    for rank, person in enumerate(sorted_leaderboard, 1):
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else "⭐"

        # Using columns for proper alignment
        col1, col2, col3 = st.columns([1, 1, 3])
        with col1:
            st.image(person["image"], width=50)
        with col2:
            st.markdown(f"**{medal}**")
        with col3:
            st.markdown(f"<span class='leaderboard-text'>{person['name']} - 💰 ${person['earnings']}</span>", unsafe_allow_html=True)

elif page == "Investment Tips":
    st.subheader("📈 Investment Tips")
    investment_tips = [
        "Diversify your portfolio for long-term growth!",
        "Invest in index funds for low-risk, steady returns!",
        "Always have an emergency fund before investing!",
        "Consider real estate for passive income streams!"
    ]
    if st.button("Get an Investment Tip 📊"):
        tip = random.choice(investment_tips)
        st.success(f"💡 {tip}")

add_vertical_space(2)
st.write("✨ Created with ❤️ by Alishba Moin")
