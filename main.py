import logging
import pickle
import random
import time
import os
import securestuff

import telegram
from telegram.ext import CommandHandler, Updater

from err import error_callback
from misc import meme_bag, shuffle_bag
from responces import (fishstick, petrostickers, quotes, rabotaetliresplist,
                       responceslist, version)
from os.path import join

rabotaetlist = shuffle_bag(rabotaetliresplist, 'rabotaetli')
stickers = shuffle_bag(petrostickers, 'stickers')
responces = shuffle_bag(responceslist, 'responces')
fish = shuffle_bag(fishstick, 'fish')
memes = meme_bag()


def rabotaetli(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=rabotaetlist.pop())
        print(('{0}||{1}:{2}'.format(time.asctime( time.localtime(time.time())), update.message.from_user.username, update.message.text)))


def ver(bot, update):
        print(('{0}||{1}:{2}'.format(time.asctime( time.localtime(time.time())), update.message.from_user.username, update.message.text)))
        bot.send_message(chat_id=update.message.chat_id, text=version)
        


def shutka(bot, update):
        print(('{0}||{1}:{2}'.format(time.asctime( time.localtime(time.time())), update.message.from_user.username, update.message.text)))        
        bot.send_message(chat_id=update.message.chat_id, text=responces.pop())
        for x in range(5):
                bot.send_sticker(chat_id=update.message.chat_id,
                                sticker=stickers.pop())


def neznayu(bot, update):
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
        print(('{0}||{1}:{2}'.format(time.asctime( time.localtime(time.time())), update.message.from_user.username, update.message.text)))
        f = open(memes.pop(), 'rb')
        bot.send_photo(chat_id=update.message.chat_id, photo=f)
        f.close


def qotd(bot, update):
        print(('{0}||{1}:{2}'.format(time.asctime( time.localtime(time.time())), update.message.from_user.username, update.message.text)))
        with open(join(os.path.dirname(os.path.realpath(__file__)), 'qotd'), 'rb') as f:
                quote = pickle.load(f)
        bot.send_message(chat_id=update.message.chat_id, text=quote)



try:
        
        updater = Updater(token=securestuff.test_token, request_kwargs=securestuff.REQUEST_KWARGS)
        print(('{0}||{1}'.format(time.asctime( time.localtime(time.time())), 'Connected to the API')))
except:
        print(('{0}||{1}'.format(time.asctime( time.localtime(time.time())), 'Exception during connection')))

 #Account for faulty token
dispatcher = updater.dispatcher


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


rabotaetli_handler = CommandHandler('rabotaetli', rabotaetli) #Make loading smarter, like a list or something, it's an eyesore(Forget it)
ver_handler = CommandHandler('ver', ver)
shutka_handler = CommandHandler('shutka', shutka)
fish_handler = CommandHandler('neznayu', neznayu)
nebo_handler = CommandHandler('nebo', nebo)
topshutka_handler = CommandHandler('topshutka', topshutka)
mem_handler = CommandHandler('mem', mem)
qotd_handler = CommandHandler('qotd', qotd)
dispatcher.add_handler(rabotaetli_handler)
dispatcher.add_handler(ver_handler)
dispatcher.add_handler(shutka_handler)
dispatcher.add_handler(fish_handler)
dispatcher.add_handler(nebo_handler)
dispatcher.add_handler(topshutka_handler)
dispatcher.add_handler(mem_handler)
dispatcher.add_handler(qotd_handler)
dispatcher.add_error_handler(error_callback)


updater.start_polling()
print(('{0}||{1}'.format(time.asctime( time.localtime(time.time())), 'Starting polling')))
updater.idle()


#
