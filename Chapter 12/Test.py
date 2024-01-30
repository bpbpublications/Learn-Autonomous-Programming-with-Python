from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses.
pairs = [
[
r"What is your name?",
["My name is Chatbot, and I'm here to help you.",]
],
[
r"my name is (.*)",
["Hello %1, How can I help you today?",]
],
# Add more patterns and responses as needed
]

print("Hi, I'm your new chatbot friend and I'm here to help you! May I know your name?")

# Create Chat object with pairs and reflections
chat = Chat(pairs, reflections)

# Start conversation
chat.converse(quit="No")
