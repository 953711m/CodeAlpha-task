import nltk
import random
from nltk.chat.util import Chat, reflections


patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ['I am fine,']),
    (r'what is your name?', ['My Name Is ChatBot']),
    (r'what is your owner name?', ['Manish Makwana!']),
    (r'bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!']),
    (r'', ["Sorry I cant Understand"])
]

chatbot = Chat(patterns, reflections)


def let_conversation():
    print("Welcome to the ChatBot! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("ChatBot:", response)


let_conversation()
