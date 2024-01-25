import discord 
import os
from dotenv import load_dotenv
from neuralintents import BasicAssistant

# Instantiate the BasicAssistant class with a specific model name
chatbot = BasicAssistant(intents_data='intents.json', model_name='chatbot_model')

# Load the model using an absolute path
model_path = os.path.abspath('path/to/your/model_directory/chatbot_model.keras')
chatbot.load_model(model_path)

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    
    if message.content.startswith("$pixelpioneer"):
        response = chatbot.request(message.content[7:])
        await message.channel.send(response)

client.run(TOKEN)
