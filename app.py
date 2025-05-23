import streamlit as st
from bible_mood_matcher import load_verses, match_verses_by_mood

# Load verses from Excel
df = load_verses()

# Streamlit UI
st.set_page_config(page_title="Divine Voice", layout="centered")
st.title("📖 Divine Voice - Bible Verse Companion")

# Input fields
name = st.text_input("What's your name?")
age_group = st.selectbox("Choose your age group", ["5–10 (Kids)", "10–15 (Teen)", "15–25 (Youth)", "25–50 (Adult)", "50+ (Senior)"])
occupation = st.selectbox("What's your occupation?", ["Student", "Working Professional", "Retired"])
mood = st.selectbox("What's your current mood?", [
    "Happy", "Sad", "Worried", "Thankful", "Lonely",
    "Confused", "Peaceful", "Lost", "Afraid", "Hopeful"
])

# Generate response
if st.button("Get Verse"):
    if name and mood:
        st.subheader(f"Hello {name}, here are verses just for you:")
        verses = match_verses_by_mood(mood, df)
        for i, verse in enumerate(verses, start=1):
            st.markdown(f"**{i}.** {verse}")
    else:
        st.warning("Please enter your name and select your mood.")
