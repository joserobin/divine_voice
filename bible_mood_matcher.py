import pandas as pd
import random

def load_bible_data(file_path):
    """
    Load the Bible data and return DataFrame and the verse text column name.
    """
    df = pd.read_excel(file_path)

    # Check if "Text" column is present
    if "Text" in df.columns:
        verse_col = "Text"
    else:
        # Try to detect the verse text column
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
    """
    try:
        matched = df[df[verse_col].str.lower().str.contains(mood.lower(), na=False)]
    except KeyError as e:
        raise KeyError(f"Column '{verse_col}' not found in DataFrame columns: {df.columns.tolist()}") from e

    if matched.empty:
        return df.sample(3)[verse_col].tolist()
    else:
        return matched.sample(min(3, len(matched)))[verse_col].tolist()
