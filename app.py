import streamlit as st
from bible_mood_matcher import load_bible_data, match_verses_by_mood

st.set_page_config(page_title="Divine Voice", layout="centered")

st.title("📖 Divine Voice – Personalized Bible Verse App")

# Input fields
name = st.text_input("👤 Your Name")

age_group = st.selectbox("🎂 Age Group", ["5–10 (Kids)", "10–15 (Teen)", "15–25 (Youth)", "25–50 (Adult)", "50+ (Senior)"])

occupation = st.selectbox("💼 Occupation", ["Student", "Working Professional", "Retired"])

mood = st.selectbox(
    "🧠 How are you feeling today?",
    ["Peaceful", "Anxious", "Grateful", "Lonely", "Sad", "Joyful", "Lost", "Tired", "Hopeful", "Fearful", "Confused"]
)

# Load Bible Data
try:
    df, verse_col = load_bible_data("englishBible.xlsx")
except Exception as e:
    st.error(f"Failed to load Bible data: {e}")
    st.stop()

# Button to get verse
if st.button("✨ Get a Bible Verse"):
    with st.spinner("Searching for a meaningful verse..."):
        try:
            verses = match_verses_by_mood(mood, df, verse_col)
            st.success(f"Here are verses for you, {name or 'Friend'}:")
            for i, verse in enumerate(verses, 1):
                st.markdown(f"**{i}.** {verse}")
        except Exception as e:
            st.error(f"Something went wrong: {e}")
