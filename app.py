import streamlit as st
import openai

# Set your OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("📖 Divine Voice: Personalized Bible Verse Companion")

st.markdown("This app shares Bible verses based on your age, mood, and life stage.")

# --- Input Fields ---
name = st.text_input("Your Name")

age_group = st.selectbox("Your Age Group", ["5-10 (Kids)", "10-15 (Teen)", "15-25 (Youth)", "25-50 (Adult)", "50+ (Senior)"])

occupation = st.selectbox("What best describes you?", ["Student", "Working Professional", "Retired", "Homemaker", "Other"])

mood_options = ["Anxious", "Grateful", "Confused", "Sad", "Happy", "Lonely", "Hopeful", "Tired", "Motivated", "Other"]
selected_mood = st.selectbox("How are you feeling right now?", mood_options)

custom_mood = ""
if selected_mood == "Other":
    custom_mood = st.text_input("Please describe your current mood")

# Final mood used in prompt
final_mood = custom_mood if selected_mood == "Other" else selected_mood

# --- Function to Get Bible Response ---
def get_bible_response(name, age_group, occupation, mood):
    prompt = (
        f"The user is {name}, aged {age_group}, and is a {occupation}. "
        f"They are currently feeling '{mood}'. Recommend a Bible verse suitable for them and explain it "
        f"simply, offering hope and comfort based on their life stage."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a wise and kind Bible teacher."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.8
    )

    return response.choices[0].message.content

# --- Submit Button ---
if st.button("Get My Verse"):
    if not name or not final_mood:
        st.warning("Please complete all the required fields.")
    else:
        with st.spinner("Reflecting..."):
            output = get_bible_response(name, age_group, occupation, final_mood)
            st.subheader("📜 Your Personalized Bible Verse & Explanation")
            st.write(output)
