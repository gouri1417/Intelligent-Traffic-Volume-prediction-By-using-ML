import streamlit as st
import pickle
import pandas as pd

# -------------------------------------------------
# Load trained pipeline
# -------------------------------------------------
with open("traffic_pipeline.pkl", "rb") as f:
    pipeline = pickle.load(f)

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Traffic Volume Prediction",
    layout="centered"
)

st.title("🚦 Traffic Volume Prediction")
st.markdown("Enter traffic and weather details to **predict traffic volume**.")

# -------------------------------------------------
# Input Section
# -------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    temp = st.number_input("Temperature (K)", value=300.0)
    rain = st.number_input("Rain (mm)", value=0.0)
    snow = st.number_input("Snow (mm)", value=0.0)
    month = st.number_input("Month", min_value=1, max_value=12, value=6)
    day = st.number_input("Day", min_value=1, max_value=31, value=15)
    hour = st.number_input("Hour", min_value=0, max_value=23, value=12)

with col2:
    minute = st.number_input("Minute", min_value=0, max_value=59, value=0)
    second = st.number_input("Second", min_value=0, max_value=59, value=0)
    weekday = st.number_input("Weekday (0=Mon, 6=Sun)", min_value=0, max_value=6, value=2)
    rush = st.selectbox("Is Rush Hour?", options=[0, 1])
    weather = st.selectbox(
        "Weather",
        options=["Clear", "Clouds", "Rain", "Snow", "Thunderstorm", "Drizzle", "Fog", "Mist"]
    )

# -------------------------------------------------
# Prediction
# -------------------------------------------------
if st.button("🚦 Predict Traffic Volume"):
    try:
        sample = {
            "temp": [float(temp)],
            "rain": [float(rain)],
            "snow": [float(snow)],
            "weather": [weather],
            "month": [int(month)],
            "day": [int(day)],
            "hour": [int(hour)],
            "minute": [int(minute)],
            "second": [int(second)],
            "weekday": [int(weekday)],
            "is_rush_hour": [int(rush)]
        }

        sample_df = pd.DataFrame(sample)

        prediction = pipeline.predict(sample_df)[0]

        st.success(f"🚦 Predicted Traffic Volume: **{int(prediction)}**")

    except Exception as e:
        st.error(f"❌ Invalid input or prediction error: {e}")
