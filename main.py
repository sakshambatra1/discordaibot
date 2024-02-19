import discord
import os
import openai
from dotenv import load_dotenv

load_dotenv()
TOKEN = your_discord_token

OPENAI_API_KEY = your_api_key

openai.api_key = OPENAI_API_KEY

# Define your intents
intents = discord.Intents.default()  # This enables the default intents, including messages
intents.messages = True  # Ensure that your bot can receive messages

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f"Message received: {message.content}")  # Debugging line
    if message.author == client.user:
        return

    if message.content.startswith("$bot"):
        command_text = message.content[len("$bot"):].strip()
        print(f"Processing command: {command_text}")
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Adjust the engine as necessary
            prompt=f"The following is a question from a Discord user: '{command_text}'\n\nHow should the chatbot respond?",
            temperature=0.7,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        await message.channel.send(response.choices[0].text.strip())

    except Exception as e:
        print(f"Error calling OpenAI: {e}")
        await message.channel.send("Sorry, I encountered an error processing your request.")

client.run(TOKEN)