from logic import DB_Manager
from config import *
from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telebot import types
hideBoard = types.ReplyKeyboardRemove()

genres = [(_,) for _ in (
['Экшен', 'Приключенческий', 'Файтинг/драка', 'Музыкальная (?)',
 'Платформенная (?)', 'Головоломка', 'Гонки', 'Ролевая игра', 'Шутер', 'Симуляция', 'Спортивная', 'Стратегия'])]

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, """Привет! Я бот ассистент по играм
Помогу тебе выбрать игру и узнать больше о них!) 
""")

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id,
        """
        Вот команды которые могут тебе помочь:

     
        ....""")

@bot.message_handler(commands=['select'])
def select(message):
     None

if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    bot.infinity_polling()