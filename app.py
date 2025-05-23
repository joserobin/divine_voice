import streamlit as st
from openai import OpenAI

# Load API key securely from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set up page
st.set_page_config(page_title="Divine Voice", layout="centered")
st.title("📖 Divine Voice – Personalized Bible Verse Generator")

# User inputs
name = st.text_input("Your Name")
age_group = st.selectbox("Select Your Age Group", [
    "Kids (5–10)", "Teen (10–15)", "Youth (15–25)", "Adult (25–50)", "Older Adult (50+)"
])
occupation = st.selectbox("What best describes you?", [
    "Student", "Working Professional", "Retired"
])
mood = st.text_input("What are you feeling or thinking about right now? (e.g., anxious, grateful, confused)")

# OpenAI request function
def get_bible_verse_and_explanation(name, age_group, occupation, mood):
    prompt = (
        f"A person named {name}, who is a {occupation} and belongs to the {age_group} age group, "
        f"is currently feeling or thinking: '{mood}'. Suggest a suitable Bible verse that matches their mood. "
        f"Then provide a short, age-appropriate explanation to comfort or guide them."
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a kind and insightful Christian guide. You respond with meaningful Bible verses "
                    "and explain them simply, based on the user's life stage and emotional state."
                )
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )

    return response.c
