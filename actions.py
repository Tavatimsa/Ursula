# bot.py
import logging, os, json, requests

URL = os.getenv('DOWNLOAD_URL')
FILENAME = os.getenv('DOWNLOAD_FILENAME')


async def greeting(member):
    logging.info(f'{member} has joined.')
    await member.create_dm()
    await member.dm_channel.send(
        f'Üdv a BloodTracken, {member.name}!\nRemélem, jól érzed majd magad nálunk :)'
    )


async def memes():
    resp = requests.get(URL, allow_redirects=True)
    memes_json = json.loads(resp.text)
    open(FILENAME, 'wb').write(resp.content)
    json_data = json.loads(open(FILENAME).read())
    meme = requests.get(json_data["data"]["children"][10]["data"]["url"], allow_redirects=True)
    img_urls = []
    for item in json_data["data"]["children"]:
        itemurl = item["data"]["url"]
        if any(itemurl[-4:] == ext for ext in ('.jpg', '.png')):
            img_urls.append(itemurl)