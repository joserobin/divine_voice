openai.lib._old_api.APIRemovedInV1: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
Traceback:

File "/mount/src/divine_voice/app.py", line 54, in <module>
    output = get_bible_response(name, age_group, occupation, final_mood)
File "/mount/src/divine_voice/app.py", line 36, in get_bible_response
    response = openai.ChatCompletion.create(
        model="gpt-4",
    ...<5 lines>...
        temperature=0.8
    )
File "/home/adminuser/venv/lib/python3.13/site-packages/openai/lib/_old_api.py", line 39, in __call__
    raise APIRemovedInV1(symbol=self._symbol)
