# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!\n')

    for guild in client.guilds:
            guilds = '- ' + guild.name + ' ' + str(guild.id) + '\n'
    print(f'The bot is curently member of the following guilds:\n{guilds}')

client.run(TOKEN)