import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
import time

TIME_ZONES = [
    "UTC",  # Universal Time
    "Asia/Karachi",  # Pakistan Standard Time (PST)
    "America/New_York",  # Eastern Time (ET) - USA
    "America/Los_Angeles",  # Pacific Time (PT) - USA
    "Europe/London",  # United Kingdom (GMT/BST)
    "Australia/Sydney",  # Australian Eastern Standard Time (AEST)
    "Asia/Kolkata",  # Indian Standard Time (IST)
    "Asia/Shanghai",  # China Standard Time (CST)
    "Asia/Tokyo",  # Japan Standard Time (JST)
    "Europe/Berlin",  # Germany (CET)
    "America/Sao_Paulo",  # Brazil (Brasília Time)
    "Europe/Moscow",  # Russia (Moscow Standard Time)
    "Africa/Johannesburg",  # South Africa Standard Time (SAST)
    "Asia/Riyadh",  # Saudi Arabia (AST)
    "Asia/Dubai",  # United Arab Emirates (GST)
    "Asia/Seoul"  # South Korea Standard Time (KST)
]

st.sidebar.title("Time Zone App")
sidebar_features = st.sidebar.radio("Go to:", [
    "Check Time in Multiple Zones", 
    "Time Converter", 
    "Time Difference Calculator"
    ])

# Feature -> 1
if sidebar_features == "Check Time in Multiple Zones":
    st.header("🌐 Check Time in Multiple Zones")

    # User selects multiple time zones to check the current time
    selected_tz = st.multiselect("Select Time Zones:", TIME_ZONES, default=["UTC", "Asia/Karachi"])

    # Display header for the time section
    st.write("### 🕰 Current Time in Selected Zones")

    # Loop through selected time zones and display the current time
    for tz in selected_tz:
        current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
        st.write(f"**{tz}**: {current_time}")  # Show time for each selected zone


# Feature -> 2
elif sidebar_features == "Time Converter":
    st.header("🔀 Time Converter")

    # User selects a date and time for conversion
    custom_date = st.date_input("Select a Date", value=datetime.today())
    current_time = st.time_input("Select Time", value=datetime.now().time())

    # Choose time zones for conversion
    from_tz = st.selectbox("Convert From", TIME_ZONES, index=0)
    to_tz = st.selectbox("Convert To", TIME_ZONES, index=1)

    if st.button("Convert Time"):
        # Combine date and time with the selected timezone
        dt = datetime.combine(custom_date, current_time, tzinfo=ZoneInfo(from_tz))

        # Convert to the target timezone
        converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")

        st.success(f"✅ Time in {to_tz}: {converted_time}")


# Feature -> 3
elif sidebar_features == "Time Difference Calculator":
    st.header("⏱ Time Difference Calculator")

    # Select time zones from the dropdown
    time_zone1 = st.selectbox("First Timezone", TIME_ZONES, index=0)
    time_zone2 = st.selectbox("Second Timezone", TIME_ZONES, index=1)

    if st.button("Calculate Difference"):
        now_utc = datetime.now(ZoneInfo("UTC"))  # Get current UTC time

        # Convert current UTC time to selected time zones
        tz1_time = now_utc.astimezone(ZoneInfo(time_zone1))
        tz2_time = now_utc.astimezone(ZoneInfo(time_zone2))

        # Calculate the time difference in hours
        diff_hours = (tz1_time.utcoffset().total_seconds() - tz2_time.utcoffset().total_seconds()) / 3600

        # Display the time difference 
        if diff_hours > 0:
            st.info(f"📍 {time_zone1} is ahead of {time_zone2} by {diff_hours:.2f} hours")
        elif diff_hours < 0:
            st.info(f"📍 {time_zone1} is behind {time_zone2} by {abs(diff_hours):.2f} hours")
        else:
            st.info("Both time zones are the same!")  # If there's no difference
