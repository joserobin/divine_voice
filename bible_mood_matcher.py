import pandas as pd
import random

def load_verses(file_path="New Testament.xlsx"):
    try:
        df = pd.read_excel(file_path)
        df.dropna(subset=["Verse Text"], inplace=True)
        return df
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return pd.DataFrame()

def match_verses_by_mood(mood, df):
    mood = mood.strip().lower()

    if 'Mood' in df.columns:
        matched = df[df['Mood'].str.lower().str.contains(mood, na=False)]
    else:
        matched = df[df['Verse Text'].str.lower().str.contains(mood, na=False)]

    if matched.empty:
        return ["No specific match found. Here's a random verse: " + random.choice(df['Verse Text'].tolist())]

    return matched['Verse Text'].sample(min(3, len(matched))).tolist()
