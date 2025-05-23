import streamlit as st
from openai import OpenAI
import pyttsx3

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Text-to-speech engine
engine = pyttsx3.init()

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

def get_bible_response(name, age_group, occupation, mood):
    prompt = (
        f"The user is {name}, aged {age_group}, and is a {occupation}. "
        f"They are currently feeling '{mood}'. Recommend a suitable Bible verse and explain it "
        f"simply, offering hope and comfort for their current state."
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a compassionate Bible teacher who offers encouragement and wisdom."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.8
    )

    return response.choices[0].message.content

# Streamlit UI
st.set_page_config(page_title="Divine Voice", layout="centered")

st.title("📖 Divine Voice - Bible Verse Companion")
st.subheader("Get a personalized Bible verse based on your feelings")

# User Inputs
name = st.text_input("Enter your name")

age_group = st.selectbox("Select your age group", [
    "Kids (5-10)", "Teen (10-15)", "Youth (15-25)", "Adult (25-50)", "Senior (50+)"
])

occupation = st.selectbox("Select your occupation", [
    "Student", "Working Professional", "Homemaker", "Retired", "Other"
])

mood = st.selectbox("How are you feeling today?", [
    "Happy 😊", "Sad 😢", "Anxious 😟", "Lonely 😔", "Thankful 🙏", "Lost 😕", "Angry 😠", "Hopeful 🌈"
])

if st.button("✨ Get Bible Verse"):
    with st.spinner("Fetching a verse for you..."):
        response = get_bible_response(name, age_group, occupation, mood)
        st.markdown("### ✝️ Bible Verse & Explanation")
        st.write(response)

        if st.button("🔊 Listen"):
            text_to_speech(response)
