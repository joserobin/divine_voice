import streamlit as st
from openai import OpenAI

# Initialize OpenAI client (use secret key via Streamlit Cloud secrets)
client = OpenAI()

st.set_page_config(page_title="Divine Voice", layout="centered")
st.title("📖 Divine Voice – Personalized Bible Verse Generator")

# Input fields
name = st.text_input("Your Name")
age_group = st.selectbox("Select Your Age Group", [
    "Kids (5–10)", "Teen (10–15)", "Youth (15–25)", "Adult (25–50)", "Older Adult (50+)"
])
occupation = st.selectbox("What best describes you?", [
    "Student", "Working Professional", "Retired"
])
mood = st.text_input("What are you feeling or thinking about right now? (e.g., anxious, grateful, confused)")

# Function to generate response
def get_bible_verse_and_explanation(name, age_group, occupation, mood):
    prompt = (
        f"Act as a Christian guide. A user named {name}, who is a {occupation} in the {age_group} age group, "
        f"is feeling '{mood}'. Suggest a relevant Bible verse and provide a short explanation. "
        f"Make the explanation age-appropriate and easy to understand."
