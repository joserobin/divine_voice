def match_verses_by_mood(mood, df, verse_col):
    """
    Match Bible verses based on a mood keyword.
    """
    try:
        # Ensure the verse column is all strings
        df[verse_col] = df[verse_col].astype(str)

        matched = df[df[verse_col].str.lower().str.contains(mood.lower(), na=False)]
    except KeyError as e:
        raise KeyError(f"Column '{verse_col}' not found in DataFrame columns: {df.columns.tolist()}") from e

    if matched.empty:
        return df.sample(3)[verse_col].tolist()
    else:
        return matched.sample(min(3, len(matched)))[verse_col].tolist()
