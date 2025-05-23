import streamlit as st
from bible_mood_matcher import load_bible_data, match_verses_by_mood

st.set_page_config(page_title="Divine Voice", page_icon="✨", layout="centered")

st.title("✨ Divine Voice: Get Bible Verses by Mood")
st.markdown("Find comfort, guidance, and encouragement from the Bible based on how you feel.")

# Mood input
mood = st.text_input("What are you feeling right now? (e.g., anxious, grateful, lost, hopeful)")

# Load the Bible data
try:
    df, verse_col = load_bible_data("englishBible.xlsx")
except Exception as e:
    st.error(f"Failed to load Bible data: {e}")
    st.stop()

# Button to generate verses
if st.button("✨ Get a Bible Verse"):
    if not mood:
        st.warning("Please enter your current mood to receive relevant Bible verses.")
    else:
        try:
            verses = match_verses_by_mood(mood, df, verse_col)
            st.subheader("📖 Here are some Bible verses for you:")
            for verse in verses:
                st.markdown(f"✅ *{verse}*")
        except Exception as e:
            st.error(f"Error finding verses: {e}")

