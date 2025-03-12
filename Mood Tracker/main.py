import streamlit as st 
import pandas as pd 
import datetime 
import csv 
import os 

# Define the file where mood data will be stored
MOOD_FILE = "mood_log.csv"

# Function to load mood data from the CSV file
def load_mood_data():
    # Check if the file exists
    if not os.path.exists(MOOD_FILE):
        # If not, return an empty DataFrame with specified columns
        return pd.DataFrame(columns=["Date", "Mood"])
    # If the file exists, read the data into a DataFrame
    return pd.read_csv(MOOD_FILE)

# Function to save mood data to the CSV file
def save_mood_data(date, mood):
    # Open the file in append mode
    with open(MOOD_FILE, "a") as file:
        # Create a CSV writer object
        writer = csv.writer(file)
        # Write the date and mood as a new row in the file
        writer.writerow([date, mood])

# Streamlit App UI configuration
st.set_page_config(page_title="Mood Tracker", layout="centered")
st.title("📅 Mood Tracker App")

# Get today's date
today = datetime.date.today()

# Display a subheader asking the user how they are feeling today
st.subheader("How are your feeling today?")

# Create a dropdown menu for the user to select their mood
mood = st.selectbox("Choose your mood", [
    "Happy", 
    "Sad", 
    "Neutral", 
    "Angry", 
    "Excited", 
    "Tired"
])

# If the user clicks the "Log Mood" button
if st.button("Log Mood"):
    # Save the selected mood and today's date to the CSV file
    save_mood_data(today, mood)
    # Display a success message
    st.success("✅ Mood Logged Successfully!")

# Load the mood data from the CSV file
data = load_mood_data()

# If there is any data loaded
if not data.empty:
    # Convert the "Date" column to datetime format
    data["Date"] = pd.to_datetime(data["Date"])

    # Calculate the count of each mood
    mood_counts = data["Mood"].value_counts()

    # 📈 Mood Changes Over Time (Line Chart)
    st.subheader("📈 Mood Changes Over Time")
    # Group moods per date and count them
    mood_trends = data.groupby("Date")["Mood"].count()
    # Display the mood trends as a line chart
    st.line_chart(mood_trends)

    # 📊 Most Frequent Moods (Bar Chart)
    st.subheader("📊 Most Frequent Moods")
    # Display the count of each mood as a bar chart
    st.bar_chart(mood_counts)

    # Provide a download button for the user to download the mood data as a CSV file
    st.download_button(
        label="📥 Download Mood Data",
        data=data.to_csv(index=False),
        file_name="mood_data.csv",
        mime="text/csv"
    )

    st.write("Build with ❤️ by [ALISHBA MOIN](https://github.com/Alishba-moin)")

