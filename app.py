import streamlit as st
import pandas as pd
from openai import OpenAI
from bible_mood_matcher import match_verses_by_mood
import os

# Load the Excel file
@st.cache_data
def load_data():
    df = pd.read_excel("englishBible.xlsx")
    return df

df = load_data()

# UI Elements
st.title("📖 Divine Voice: Bible Verse Generator")
st.markdown("---")

name = st.text_input("🙏 Your Name")
age_group = st.selectbox("🎂 Age Group", ["Kids (5-10)", "Teen (10-15)", "Youth (15-25)", "Adult (25-50)", "Senior (50+)"])
occupation = st.selectbox("💼 Occupation", ["Student", "Working Professional", "Homemaker", "Retired", "Other"])
mood = st.selectbox("🧠 How are you feeling today?", ["Happy", "Sad", "Anxious", "Thankful", "Lonely", "Grateful", "Fearful", "Tired", "Excited"])

if st.button("✨ Get a Bible Verse"):
    if name and mood:
        with st.spinner("Finding a verse just for you..."):
            verses = match_verses_by_mood(mood, df)

            if verses:
                st.success(f"Dear {name}, here are some verses for you:")
                for i, verse in enumerate(verses):
                    st.markdown(f"**{i+1}.** {verse}")
            else:
                st.warning("Sorry, we couldn't find a matching verse. Try a different mood.")
    else:
        st.warning("Please enter your name and choose your mood.")
