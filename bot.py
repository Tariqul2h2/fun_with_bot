from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus


CORPUS_FILE = "friend.txt"
NAME = input('input someones name: ')
YOUR_NAME = input('input your name: ')
EXIT = ('bye', 'gelam', 'tata')
print('Exit conditions are:',EXIT)

chatbot = ChatBot("Chatbot")

trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)

while True:
    query = input(f'{YOUR_NAME}: ')
    if query in EXIT:
        break
    else:
        print(f"{NAME}: {chatbot.get_response(query)}")