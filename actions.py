# bot.py
import logging, discord


async def greeting(member):
    logging.info(f'{member} has joined.')
    await member.create_dm()
    await member.dm_channel.send(
        f'Üdv a BloodTracken, {member.name}!\nRemélem, jól érzed majd magad nálunk :)'
    )