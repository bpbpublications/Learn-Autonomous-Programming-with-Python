import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"My name is (.*)",
        ["Hello %1, How are you?",]
    ],
    [
        r"(I'm|good|good,|I am)",
        ["How can I help you?\nPlease select one from the following:" \
         "\n1)New Software Installation\n2)Issue with Existing Software",]
    ], 
    [
        r"(.*) Installation",
        ["Could you please mention the name of the software? Please type 'Software:'" \
         "before mentioning the software name. Thanks!",]
    ],
    [
        r"(.*) Existing",
        ["Please select the issue from the following:" \
         "\n1)Version needs Upgradation\n2)Uninstall Software",]
    ],
    [
        r"(Version|Uninstall)",
        ["Thanks for your patience. Someone from the IT team " \
         "would reach out to you to resolve your issue.Is there anything else" \
         "I could help you with?",]
    ],
    [
        r"Software:(.*)",
        ["Thanks for your patience. I am assignining this ticket to someone from " \
         "the IT team who shall help you install %1.Is there anything else I could help you with?",]
    ],
    [
        r"No",
        ["Thank you. Have a great day!",]
    ],
]

print("Hi, I'm your new chatbot friend and I'm here to help you! May I know your name?")

chat = Chat(pairs, reflections)
chat.converse(quit="No")

