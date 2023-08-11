import openai
import os

openai.api_key = open("openai_key.txt","r").read()

prompt = "Hello ChatGPT"
# prompt = "Create a test scenario for this release note: Make tab context menu less cluttered by adding sub-menu."
message = {"role": "user", "content": prompt}

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[message])

print(chat_completion)