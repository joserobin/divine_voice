import pandas as pd
import random

# Mood → Malayalam keywords mapping
mood_keywords_map = {
    "Sad / Discouraged": ["ആശ്വാസം", "പ്രത്യാശ", "ശക്തി", "സ്നേഹം"],
    "Anxious / Fearful": ["സമാധാനം", "വിശ്വാസം", "ഭയം ഇല്ല", "വിശ്രമം", "ധൈര്യം"],
    "Happy / Grateful": ["സന്തോഷം", "ആനന്ദം", "സ്തുതി", "ആശംസ", "പുണ്യം"],
    "Angry / Hurt": ["ക്ഷമ", "ദയ", "സുഖം", "സൗഖ്യം", "പരിഹാരം"],
    "Confused / Lost": ["മാർഗം", "ജ്ഞാനം", "സത്യമാണ്", "വഴി", "വെളിച്ചം"],
    "Lonely / Isolated": ["സാന്നിധ്യം", "സ്നേഹം", "കൈ ചേർക്കുക", "കൂടെയുണ്ട്"]
}

def get_bible_verses_for_mood(mood, file_path="New Testament.xlsx", max_results=5):
    if mood not in mood_keywords_map:
        return ["Invalid mood selected. Please try again."]
    
    keywords = mood_keywords_map[mood]

    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        return [f"Error reading file: {e}"]

    if 'Verse' not in df.columns or 'Reference' not in df.columns:
        return ["Invalid file format. Columns 'Verse' and 'Reference' are required."]

    matching_verses = df[df['Verse'].apply(lambda verse: any(keyword in str(verse) for keyword in keywords))]

    if matching_verses.empty:
        return ["No verses found for the selected mood."]

    sampled = matching_verses.sample(min(len(matching_verses), max_results))

    return [f"{row['Reference']}: {row['Verse']}" for _, row in sampled.iterrows()]
