from os import getenv
from dotenv import load_dotenv

import bot

load_dotenv()
TOKEN = getenv('TOKEN')

client = bot.RandomOrgBot()

client.run(TOKEN)