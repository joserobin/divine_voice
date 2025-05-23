import streamlit as st
from bible_mood_matcher import load_verses, match_verses_by_mood

st.set_page_config(page_title="Divine Voice - Bible Verse App", layout="centered")

st.title("📖 Divine Voice")
st.subheader("Receive a Bible verse based on your mood and situation")

# User Inputs
name = st.text_input("Your Name")

age_group = st.selectbox("Select Your Age Group", ["Kids (5–10)", "Teen (10–15)", "Youth (15–25)", "Adult (25–50)", "Senior (50+)"])

occupation = st.selectbox("Select Your Role", ["Student", "Working Professional", "Retired", "Other"])

mood = st.selectbox(
    "How are you feeling today?",
    ["Happy", "Sad", "Anxious", "Grateful", "Lonely", "Worried", "Confused", "Angry", "Fearful", "Hopeless", "Forgiven", "Blessed"]
)

# Load Bible data
df = load_verses("englishBible.xlsx")

if st.button("✨ Get a Bible Verse"):
    if df.empty:
        st.error("Failed to load Bible data. Please check the file.")
    else:
        with st.spinner("Finding a verse for you..."):
            verses = match_verses_by_mood(mood, df)
            st.success(f"Hello {name or 'Friend'}! Here are some verses for you:")
            for verse in verses:
                st.write(f"📜 {verse}")
