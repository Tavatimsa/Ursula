# bot.py
import logging
import requests
from requests.auth import HTTPBasicAuth
from praw import Reddit
from atlassian import Bamboo
from os import getenv
from dotenv import load_dotenv

load_dotenv()
REDDIT_CLIENT_ID = getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = getenv('REDDIT_CLIENT_SECRET')
REDDIT_USER_AGENT = getenv('REDDIT_USER_AGENT')
BAMBOO_URL = getenv('BAMBOO_URL')
BAMBOO_USERNAME = getenv('BAMBOO_USERNAME')
BAMBOO_PASSWORD = getenv('BAMBOO_PASSWORD')
BAMBOO_PROJECT = getenv('BAMBOO_PROJECT')
BAMBOO_PLAN = getenv('BAMBOO_PLAN')
BAMBOO_ARTIFACT = getenv('BAMBOO_ARTIFACT')

reddit = Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT)

bamboo = Bamboo(
    url=BAMBOO_URL,
    username=BAMBOO_USERNAME,
    password=BAMBOO_PASSWORD)


async def greeting(member):
    logging.info(f'{member} has joined.')
    await member.create_dm()
    await member.dm_channel.send(
        f'Üdv a BloodTracken, {member.name}!\nRemélem, jól érzed majd magad nálunk :)'
    )


async def fun_pic(message):
    submission = reddit.subreddit('ProgrammerHumor+memes').random()
    await message.channel.send(submission.url)


async def last_prs(message):
    build_result = next(bamboo.results(project_key=BAMBOO_PROJECT, plan_key=BAMBOO_PLAN))
    dwn_url = BAMBOO_URL + '/browse/' + build_result['buildResultKey'] + BAMBOO_ARTIFACT
    resp = requests.get(dwn_url, auth = HTTPBasicAuth(BAMBOO_USERNAME, BAMBOO_PASSWORD))
    if resp.status_code is not 200:
        logging.error('Failed to get the requested file.')
    await message.channel.send('```' + resp.text + '```')