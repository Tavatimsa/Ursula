# commands.py
import actions


async def call_bot(message):
    if any(word in message.content.lower() for word in ('szia', 'hello', 'hali')):
        await message.channel.send('Szia!')
    if any(word in message.content.lower() for word in ('kösz', 'szeretlek')):
        await message.add_reaction('❤')
    if any(word in message.content.lower() for word in ('képet', 'vicceset')):
        await actions.fun_pic(message)
    if any(word in message.content.lower() for word in ('build', 'pull request')) or 'PR' in message.content:
        await actions.last_prs(message)
