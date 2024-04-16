import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

def load_data(json_file_path: str) -> dict:
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def train_model() -> ChatBot:
    bot = ChatBot('Norman', logic_adapters=[
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation",
    ])
    trainer = ListTrainer(bot)
    data = load_data('intents.json')
    for sample in data.get("intents"):
        dialogue = []
        questions = sample.get("text", [])
        responses = sample.get("responses", [])
        
        for question in questions:
            for response in responses:
                
                dialogue.append(question)
                dialogue.append(response)
        trainer.train(dialogue)
    return bot


def get_response(bot:ChatBot, question:str) -> str:
    
    answer = bot.get_response(question)
    return answer

bot = train_model()
print(get_response(bot=bot, question='Hi'))


def chat():
    # Train the model
    bot = train_model()

    # Start the conversation
    print("Hello, How can I help you today? (type 'exit' to end the conversation)")

    while True:
        # Get user input
        user_input = input("You: ")

        # Check for exit command
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Get bot's response
        response = get_response(bot, user_input)
        print(f"Bot: {response}")

# Call the chat function to start interacting with the chatbot
chat()



























#def chat():
    # Train the model
    #bot = train_model()

    # Start the conversation
    #print("Hello, How can I help you today? (type 'exit' to end the conversation)")

    #while True:
        # Get user input
        #user_input = input("You: ")

        # Check for exit command
       # if user_input.lower() == 'exit':
          #  print("Goodbye!")
           # break

        # Get bot's response
       # response = get_response(bot, user_input)
        #print(f"Bot: {response}")

