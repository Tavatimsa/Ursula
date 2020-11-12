# bot.py
import logging, os, discord
from dotenv import load_dotenv

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
    logging.info(f'{member} has joined.')
    await member.create_dm()
    await member.dm_channel.send(
        f'Üdv a BloodTracken, {member.name}! Remélem, jól érzed majd magad nálunk :)'
    )

client.run(TOKEN)
