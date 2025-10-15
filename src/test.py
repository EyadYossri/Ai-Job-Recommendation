import google.generativeai as genai

genai.configure(api_key="AIzaSyBR073Li4JZA7QXOL-Zy95RLFqhO5ZtA5o")

for m in genai.list_models():
    print(m.name)