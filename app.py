import streamlit as st
import speech_recognition as sr
from openai import OpenAI

# Load OpenAI key from secrets
client = OpenAI()

# Set up app
st.set_page_config(page_title="Divine Voice", layout="centered")
st.title("📖 Divine Voice – Bible Verse Generator")

# User Input
name = st.text_input("Enter your name:")
age_group = st.selectbox("Select your age group:", ["Kids (5-10)", "Teen (10-15)", "Youth (15-25)", "Adult (25-50)", "Older Adult (50+)"])
occupation = st.selectbox("What best describes you?", ["Student", "Working Professional", "Retired"])
mood = st.text_input("What's your current mood or concern? (e.g., anxious, happy, confused)")

# Microphone input (optional)
use_voice = st.toggle("🎙️ Use voice input")

if use_voice:
    st.info("Click the button and speak. Wait for transcription...")
    if st.button("Start Recording"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recognizer.listen(source, timeout=5)
        try:
            mood = recognizer.recognize_google(audio)
            st.success(f"You said: {mood}")
        except sr.UnknownValueError:
            st.error("Could not understand audio.")
        except sr.RequestError:
            st.error("Speech recognition service unavailable.")

# Function to call GPT-4
def get_bible_response(name, age_group, occupation, mood):
    prompt = (
        f"My name is {name}. I am a {occupation} in the {age_group} group. "
        f"My current mood or concern is: '{mood}'. Please suggest a Bible verse and explain it in an age-appropriate and easy-to-understand way."
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a compassionate Christian guide who provides age-appropriate Bible verses and explanations."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.8,
        max_tokens=500
    )

    return response.choices[0].message.content

# Display result
if st.button("🙏 Get Bible Verse and Explanation"):
    if name and mood:
        with st.spinner("Praying and finding the right verse..."):
            result = get_bible_response(name, age_group, occupation, mood)
            st.markdown("### 📜 Your Personalized Bible Message:")
            st.write(result)
    else:
        st.warning("Please enter your name and mood.")

# Optional: Add audio output with pyttsx3 (locally only)
