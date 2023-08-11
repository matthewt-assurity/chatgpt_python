import requests
from bs4 import BeautifulSoup
import openai
import os
import json

url = "https://community.notepad-plus-plus.org/topic/24802/notepad-v8-5-5-release"

openai.api_key = open("openai_key.txt","r").read()

rolePrompt = open("role.txt","r").read()
message = {"role": "user", "content": rolePrompt}
roleResponse = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[message])

# roleResponseJson = json.loads(roleResponse.toString())
print(roleResponse['choices'][0]['message']['content'])

# Send an HTTP GET request
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content
#     soup = BeautifulSoup(response.content, "html.parser")
    
#     # Find the post content section
#     post_content = soup.find("div", class_="content").select("li")

#     # Extract and print the release notes
#     if post_content:
#         for idx, i in enumerate(post_content):
#             # print(i.get_text().encode("ascii","ignore"))
#             print(f"Relase note {idx+1}: {i.get_text()}")

#     else:
#         print("Release notes not found on the page.")
# else:
#     print("Failed to retrieve the web page.")


# prompt = "Create a test case based on this release note. Relase note 1: Update to Scintilla 5.3.6 and Lexilla 5.2.6 (Implement #13940, fix #4741,  #13901, #13943, #13911)"

# rolePromptMessage = {"role": "user", "content": rolePrompt}
# roleResponseMessage = {"role": "assistant", "content": roleResponse.choices[0].content}
# message = {"role": "user", "content": prompt}

# chat_completion = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo", 
#     messages=[
#         rolePromptMessage,
#         roleResponseMessage,
#         message
#     ],
# )

# print(chat_completion)