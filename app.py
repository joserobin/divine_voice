import streamlit as st
import openai
import os

# Set page configuration
st.set_page_config(page_title="Divine Voice - Personalized Bible Wisdom")

# Title and subtitle
st.title("📖 Divine Voice")
st.subheader("Get personalized Bible verses with simple and powerful explanations.")

# Get OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# User form
with st.form("user_form"):
    name = st.text_input("👤 Enter your name")
    age_group = st.selectbox("🎂 Select your age group", ["Kids (5–10)", "Teen (10–15)", "Youth (15–25)", "Adult (25–50)"])
    occupation = st.selectbox("💼 You are a", ["Student", "Working Professional", "Retired"])
    mood = st.selectbox("🧠 How are you feeling today?", ["Happy", "Anxious", "Sad", "Lonely", "Curious", "Thankful", "Depressed", "Lost", "Energetic", "Tired"])
    submitted = st.form_submit_button("🙏 Get Verse")

# GPT Function
def get_bible_response(name, age_group, occupation, mood):
    prompt = f"""
You are a kind and wise Christian mentor.

A person named {name}, who is a {occupation} in the {age_group} age group, is feeling {mood} today.

1. Suggest a suitable Bible verse for them.
2. Provide a short, emotionally resonant explanation that is easy to understand for their age and life situation.
3. Keep the tone compassionate and uplifting.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful and loving Christian guide who explains Bible verses in an age-appropriate and compassionate way."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=500
    )

    return response['choices'][0]['message']['content']

# Output Section
if submitted:
    with st.spinner("✨ Fetching divine wisdom..."):
        result = get_bible_response(name, age_group, occupation, mood)
    st.markdown("### 📜 Here's a verse and message for you:")
    st.markdown(result)
