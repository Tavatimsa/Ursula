# bot.py
import logging, os, discord
from dotenv import load_dotenv


logging.basicConfig(filename='Ursula.log', level=logging.INFO)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    logging.info(f'{client.user} has connected to Discord!\n')

    for guild in client.guilds:
            guilds = '- ' + guild.name + ' ' + str(guild.id) + '\n'
    logging.info(f'The bot is currently member of the following guilds:\n{guilds}')

client.run(TOKEN)