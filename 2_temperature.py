from helper import add_user_message
from pprint import pprint
from helper import chat

messages = []
add_user_message(messages, "Tell me about Indian tradition. Answer in 1 sentence.")

print("Temperature = 0. Message = ")
print(chat(messages, system=None, temperature=0))

print("Temperature = 1. Message = ")
print(chat(messages, system=None, temperature=1))