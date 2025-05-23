import pandas as pd
import random

def load_verses(file_path="englishBible.xlsx"):
    try:
        df = pd.read_excel(file_path)
        df.dropna(how="all", inplace=True)
        return df
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return pd.DataFrame()

def match_verses_by_mood(mood, df):
    mood = mood.strip().lower()

    # Automatically find the verse column
    verse_col = None
    for col in df.columns:
        if "verse" in col.lower():
            verse_col = col
            break

    if not verse_col:
        return ["❌ Could not find a column containing Bible verses. Please check the Excel file."]

    # If 'Mood' column exists, filter using it first
    if 'Mood' in df.columns:
        matched = df[df['Mood'].str.lower().str.contains(mood, na=False)]
    else:
        # fallback: try to match mood in verse text
        matched = df[df[verse_col].str.lower().str.contains(mood, na=False)]

    if matched.empty:
        return ["No specific match found. Here's a random verse: " + random.choice(df[verse_col].tolist())]

    return matched[verse_col].sample(min(3, len(matched))).tolist()
