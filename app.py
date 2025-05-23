import streamlit as st

st.title("Divine Voice ✨")
st.subheader("Bringing You Closer to Jesus")

name = st.text_input("Enter your name")
mood = st.selectbox("How are you feeling today?", ["Happy", "Sad", "Anxious", "Lonely", "Confused", "Other"])

if st.button("Get a Bible Verse"):
    st.write(f"Hello {name}, here's a verse for when you're feeling {mood.lower()}.")

    # Dummy output for now
    st.write("📖 *Philippians 4:6* — 'Do not be anxious about anything...'")

    # (Later: Add OpenAI + voice output here)
