import random
import time
import securestuff
import telegram
import os
import pickle
from os.path import join
from misc import shuffle_bag, meme_bag
from responces import version




def rabotaetli(bot, update):
        rabotaetlist = shuffle_bag('rabotaetliresplist')
        if (random.randrange(0,10)>=1):
                bot.send_message(chat_id=update.message.chat_id, text=rabotaetlist.pop())
        else:
                print('PROC!')
                if update.message.from_user.id == securestuff.ilia_id:
                        update.message.reply_text("Конечно нет, Илюх, а что?")
                elif update.message.from_user.id == securestuff.leha_id:
                        update.message.reply_text("А вы как думаете, Алексей?")
                elif update.message.from_user.id == securestuff.pes_id:
                        update.message.reply_text("Нет, зато у меня не четрвертинка мозга")
                else:
                        update.message.reply_text(rabotaetlist.pop())
        print(('{0}||{1}:{2}'.format(time.asctime( time.localtime(time.time())), update.message.from_user.username, update.message.text)))


def ver(bot, update):
        print(('{0}||{1}:{2}'.format(time.asctime( time.localtime(time.time())), update.message.from_user.username, update.message.text)))
        bot.send_message(chat_id=update.message.chat_id, text=version)
        


def shutka(bot, update):
        responces = shuffle_bag('responceslist')
        stickers = shuffle_bag('petrostickers')
        print(('{0}||{1}:{2}'.format(time.asctime( time.localtime(time.time())), update.message.from_user.username, update.message.text)))        
        bot.send_message(chat_id=update.message.chat_id, text=responces.pop())
        for x in range(5):
                bot.send_sticker(chat_id=update.message.chat_id,
                                sticker=stickers.pop())


def neznayu(bot, update):
        fish = shuffle_bag('fishstick')
        print(('{0}||{1}:{2}'.format(time.asctime( time.localtime(time.time())), update.message.from_user.username, update.message.text)))
        for x in range(5):
                bot.send_sticker(chat_id=update.message.chat_id,
                                sticker=fish.pop())


def nebo(bot, update):
        print(('{0}||{1}:{2}'.format(time.asctime( time.localtime(time.time())), update.message.from_user.username, update.message.text)))
        bot.send_message(chat_id=update.message.chat_id, text='А где неба нет?')
        bot.send_sticker(chat_id=update.message.chat_id,
                        sticker='CAADAgADCwEAAvR7GQABuArOzKHFjusC')


def topshutka(bot, update):
        print(('{0}||{1}:{2}'.format(time.asctime( time.localtime(time.time())), update.message.from_user.username, update.message.text)))
        bot.send_message(chat_id=update.message.chat_id, text='https://www.youtube.com/watch?v=VQGLnaNQKds')


def mem(bot, update):
        memes = meme_bag()
        print(('{0}||{1}:{2}'.format(time.asctime( time.localtime(time.time())), update.message.from_user.username, update.message.text)))
        f = open(memes.pop(), 'rb')
        bot.send_photo(chat_id=update.message.chat_id, photo=f)
        f.close


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


def pozdravlenie(bot, update):
        print(('{0}||{1}:{2}'.format(time.asctime( time.localtime(time.time())), update.message.from_user.username, update.message.text)))
        bot.send_message(chat_id=update.message.chat_id, text='С новый годом, Овощи! Пусть для вас 2021 будет лучшим годом, все в жизни получалось и мало что удручало! Колян, тоже поздравь чтоле /kolyanpozdr')
