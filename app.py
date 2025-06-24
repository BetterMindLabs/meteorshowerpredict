import streamlit as st
import google.generativeai as genai
import datetime

# === Gemini API Setup ===
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# === Streamlit UI ===
st.set_page_config(page_title="☄️ Meteor Shower Predictor")
st.title("☄️ Meteor Shower Predictor")
st.write("Enter your location and date to check for visible meteor showers.")

# === Input Fields ===
location = st.text_input("🌍 Enter Your Location", placeholder="e.g. New Delhi, India")
target_date = st.date_input("📅 Select a Date", datetime.date.today())

# === Predict Button ===
if st.button("Check Visibility"):
    with st.spinner("Analyzing astronomical data..."):
        prompt = f"""
You are an astronomy assistant. Based on the location "{location}" and the date "{target_date}", provide:

1. Whether a meteor shower will be visible.
2. The name of the shower (if any).
3. Peak viewing time (local time).
4. Visibility conditions (general sky clarity).
5. Any tips for viewing.

Keep it concise, informative, and in bullet points.
"""
        response = model.generate_content(prompt)
        result = response.text.strip()
        
        st.subheader("🌠 Meteor Shower Forecast")
        st.markdown(result)
