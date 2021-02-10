# function to create the chatbot
# we have the read_only to false so the chatbot learns from the user input as 
def create_bot(name):
    from chatterbot import ChatBot
    Bot = ChatBot(name = name,
                  read_only = False,                  
                  logic_adapters = ["chatterbot.logic.BestMatch"],                 
                  storage_adapter = "chatterbot.storage.SQLStorageAdapter")
    return Bot

# function to train the bot with a variety of topics
# the language we have chosen is english
# we can train the bot for other languages as well
def train_all_data(Bot):
    from chatterbot.trainers import ChatterBotCorpusTrainer
    corpus_trainer = ChatterBotCorpusTrainer(Bot)
    corpus_trainer.train("chatterbot.corpus.english")

# function to train the bot with custom data
# it uses ListTrainer to train data from lists 
def custom_train(Bot, conversation):
    from chatterbot.trainers import ListTrainer
    trainer = ListTrainer(Bot)
    trainer.train(conversation)

# function to start and take responses from the chatbot
# the chatbot stays running unless a word is typed from the bye_list 
def start_chatbot(Bot):
    print('\033c')
    print("Hello, I am Debashis. How can I help you")
    bye_list = ["bye debashis", "bye", "good bye"] 
    
    while (True):
        user_input = input("me: ")   
        if user_input.lower() in bye_list:
            print("Debashis: Good bye and have a blessed day!")
            break
        
        response = Bot.get_response(user_input)
        print("Debashis:", response)