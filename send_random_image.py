"""
Created on: 24.12.2024
@author: marteszibellina
"""

import os

from dotenv import load_dotenv
import requests
from telebot import TeleBot

load_dotenv()

token = os.getenv("TOKEN")

bot = TeleBot(token)

URL = 'https://api.thecatapi.com/v1/images/search'
r = requests.get(URL).json()
random_cat = r[0].get('url')
chat_id = 1599868507
text = 'Вам телеграмма!'
bot.send_message(chat_id, text)
bot.send_photo(chat_id, random_cat)
