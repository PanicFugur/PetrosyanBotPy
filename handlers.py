import random
import time
import securestuff
import telegram
import os
import pickle
from os.path import join
from misc import shuffle_bag
from responces import version




def rabotaetli(bot, update):
        rabotaetlist = shuffle_bag('rabotaetliresplist')
        bot.send_message(chat_id=update.message.chat_id, text=rabotaetlist.pop())
        print(('{0}||{1}:{2}'.format(time.asctime( time.localtime(time.time())), update.message.from_user.username, update.message.text)))


def qotd(bot, update):
        print(('{0}||{1}:{2}'.format(time.asctime( time.localtime(time.time())), update.message.from_user.username, update.message.text)))
        with open(join(os.path.dirname(os.path.realpath(__file__)), 'qotd'), 'rb') as f:
                quote = pickle.load(f)
        bot.send_message(chat_id=update.message.chat_id, text=quote)


def start(bot, update):
        print(('{0}||{1}:{2}'.format(time.asctime( time.localtime(time.time())), update.message.from_user.username, update.message.text)))
        custom_keyboard = [['/rabotaetli - бот ты работаешь?', '/shutka - тут шутканули'], 
                   ['/qotd - мудрость дня', '/mem - покажи мне мем, бот'],
                   ['/vbros - Колян, отзовись', '/nebo - ']]

        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)

        bot.send_message(chat_id=update.message.chat_id, text='Чего желаете?',reply_markup=reply_markup)