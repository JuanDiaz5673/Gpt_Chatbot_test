import re
import openai
import json

openai.api_key = ''

print('ChatBot Assistant: Welcome, I’ll be your ChatBot assistant today. I can assist you with finding Bible verses '
      'that can be helpful, or inspiring. What can I help you with? \n')

while True:
    messages = [{"role": "system", "content": "You're a Chatbot for a Bible website that helps people find helpful "
                                              "Bible verses depending on their need. You ask if they want any more "
                                              "verses after every response, And you begin the conversation with, "
                                              "Hello I am a ChatBot that can help you find Bible verses that could "
                                              "inspire you. You will also give them some advice on their situation "
                                              "after providing the Bible verses"}]
    content = input("User: ")
    messages.append({"role": "user", "content": content})

    bible_regex = r"\b(bible|jesus|christ|god|faith|religion)\b"
    if not re.search(bible_regex, content, re.IGNORECASE):
        chat_response = "I'm sorry, that's not within my scope. Can I help you with something else?"
    else:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        chat_response = completion.choices[0].message.content

    print(f'ChatBot Assistant: {chat_response}')
    messages.append({"role": "assistant", "content": chat_response})