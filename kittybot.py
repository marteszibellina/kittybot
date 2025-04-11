"""
Created on: 24.12.2024
@author: marteszibellina
"""

import logging  # pylint: disable=import-error
import os  # pylint: disable=import-error
import requests  # pylint: disable=import-error
from dotenv import load_dotenv  # pylint: disable=import-error
from telebot import TeleBot, types  # pylint: disable=import-error

load_dotenv()

token = os.getenv('TOKEN')

bot = TeleBot(token)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    encoding='utf-8',
    level=logging.INFO)

URL = 'https://api.thecatapi.com/v1/images/search'


def get_new_image():
    """Get a new cat image."""
    try:
        response = requests.get(URL)
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)
    response = response.json()
    random_cat = response[0].get('url')
    return random_cat


@bot.message_handler(commands=['cat'])
def send_cat(message):
    """Send a cat image when the command /cat is issued."""
    chat = message.chat
    chat_id = chat.id
    bot.send_photo(chat_id, get_new_image())


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Send a welcome message when the command /start is issued."""
    chat = message.chat
    name = chat.first_name
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_newcat = types.KeyboardButton('/cat')
    keyboard.add(button_newcat)

    bot.send_message(message.chat.id,
                     f'Привет, {name}! Я котик-невротик!',
                     reply_markup=keyboard)
    bot.send_photo(message.chat.id, get_new_image())


@bot.message_handler(content_types=['text'])
def say_hi(message):
    """Say hi back!"""
    chat = message.chat
    chat_id = chat.id
    bot.send_message(chat_id, 'Ну, вот так вот...')


def main():
    """Main function."""
    bot.polling()


if __name__ == '__main__':
    main()
