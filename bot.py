# bot.py
import logging, os, discord
from dotenv import load_dotenv
import actions, commands

# logging.basicConfig(filename='Errors.log',level=logging.ERROR, format='%(asctime)s %(levelname)s: %(message)s')
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    logging.info(f'{client.user} has connected to Discord!')

    guilds = ''
    for guild in client.guilds:
        guilds += f'- {guild.name} {str(guild.id)}\n'
    if guilds == '':
        logging.error(f'The bot is currently not member of any guilds:\n')
    else:
        logging.info(f'The bot is currently member of the following guilds:\n{guilds}')


@client.event
async def on_member_join(member):
    actions.greeting(member)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'boldog szül' in message.content.lower():
        await message.channel.send('Boldog születésnapot! 🎈🎉')
    if client.user in message.mentions or str(message.channel.type) == 'private':
        await commands.call_bot(message)

client.run(TOKEN)
