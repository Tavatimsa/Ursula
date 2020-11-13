# commands.py
import logging, discord


async def call_bot(message):
    if any(word in message.content.lower() for word in ('szia', 'hello', 'hali')):
        await message.channel.send('Szia!')
    if any(word in message.content.lower() for word in ('kösz', 'szeretlek')):
        await message.add_reaction('❤')
    if any(word in message.content.lower() for word in ('mémek', 'reddit')):
        await actions.memes()
