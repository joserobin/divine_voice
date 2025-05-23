import pandas as pd
import random

def load_bible_data(file_path):
    """
    Load the Bible data from the Excel file.
    Automatically detects the column containing verse text.
    Returns the DataFrame and the name of the verse column.
    """
    df = pd.read_excel(file_path)

    # Identify the column most likely containing the verse text
    verse_col = None
    for col in df.columns:
        if "verse" in col.lower() or "text" in col.lower():
            verse_col = col
            break

    if not verse_col:
        raise ValueError("Could not find a column with verse text in the Excel file.")

    return df, verse_col


def match_verses_by_mood(mood, df, verse_col):
    """
    Match Bible verses based on a mood keyword.
    If no match is found, return random verses.
    """
    # Case-insensitive search for mood in the verse text
    matched = df[df[verse_col].str.lower().str.contains(mood.lower(), na=False)]

    if matched.empty:
        # Fallback: return random 3 verses
        fallback = df.sample(3)[verse_col].tolist()
        return fallback
    else:
        return matched.sample(min(3, len(matched)))[verse_col].tolist()
