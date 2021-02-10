from functions import *

# create chatbot 
bot = create_bot('Debashis')

# train all data
train_all_data(bot)

# train chatbot with your custom data
house_owner = [
    "Who is the owner of the house?",
    "Mark Nicholas"
]
custom_train(bot, house_owner)

# start chatbot
start_chatbot(bot)