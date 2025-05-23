import streamlit as st
import random
import openai

# Your OpenAI secret key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Step 1: Mood → List of Verses
mood_verse_map = {
    "Happy": [
        "Psalm 100:1-2 - Shout for joy to the Lord, all the earth.",
        "Nehemiah 8:10 - The joy of the Lord is your strength.",
        "Psalm 118:24 - This is the day the Lord has made; let us rejoice."
    ],
    "Anxious": [
        "Philippians 4:6 - Do not be anxious about anything...",
        "1 Peter 5:7 - Cast all your anxiety on Him because He cares for you.",
        "John 14:27 - Peace I leave with you; do not let your hearts be troubled."
    ],
    "Lonely": [
        "Deuteronomy 31:6 - God will never leave you nor forsake you.",
        "Psalm 23:4 - You are with me.",
        "Isaiah 41:10 - Do not fear, for I am with you."
    ],
    "Sad": [
        "Revelation 21:4 - He will wipe every tear.",
        "Psalm 34:18 - The Lord is close to the brokenhearted.",
        "Matthew 5:4 - Blessed are those who mourn."
    ]
}

# Step 2: UI - Mood Selection
st.title("Bible Verse Based on Your Mood 🙏")
user_mood = st.selectbox("How are you feeling today?", list(mood_verse_map.keys()))

# Step 3: Show verse options
if user_mood:
    verses = mood_verse_map[user_mood]
    selected_verse = st.radio("Select a Bible verse that speaks to you:", verses)

    # Step 4: Generate explanation
    if st.button("Get Spiritual Insight ✨"):
        with st.spinner("Praying and thinking..."):
            response = openai.ChatCompletion.create

