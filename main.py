#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import random
import time
from os.path import join

import telegram
from telegram.ext import CommandHandler, Updater

import _pickle as pickle
import securestuff
from err import error_callback
from misc import meme_bag, shuffle_bag
from responces import (fishstick, petrostickers, quotes, rabotaetliresplist,
                       responceslist, version)


def rabotaetli(bot, update):
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


def start(bot, update):
        print(('{0}||{1}:{2}'.format(time.asctime( time.localtime(time.time())), update.message.from_user.username, update.message.text)))
        custom_keyboard = [['/rabotaetli - бот ты работаешь?', '/shutka - тут шутканули'], 
                   ['/qotd - мудрость дня', '/mem - покажи мне мем, бот'],
                   ['/vbros - Колян, отзовись', '/nebo - ']]

        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)

        bot.send_message(chat_id=update.message.chat_id, text='Чего желаете?',reply_markup=reply_markup)
        


def main():
        try:
                if securestuff.production_token:
                        token = securestuff.petr_token
                else:
                        token = securestuff.test_token
                if securestuff.use_proxy == True:
                        updater = Updater(token=token, request_kwargs=securestuff.REQUEST_KWARGS)
                else:
                        updater = Updater(token=token)
                
                print(('{0}||{1}'.format(time.asctime( time.localtime(time.time())), 'Connected to the API')))
        except:
                print(('{0}||{1}'.format(time.asctime( time.localtime(time.time())), 'Exception during connection')))

        #Account for faulty token
        dispatcher = updater.dispatcher


        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

        dispatcher.add_handler(CommandHandler('rabotaetli', rabotaetli))
        dispatcher.add_handler(CommandHandler('ver', ver))
        dispatcher.add_handler(CommandHandler('shutka', shutka))
        dispatcher.add_handler(CommandHandler('neznayu', neznayu))
        dispatcher.add_handler(CommandHandler('nebo', nebo))
        dispatcher.add_handler(CommandHandler('topshutka', topshutka))
        dispatcher.add_handler(CommandHandler('mem', mem))
        dispatcher.add_handler(CommandHandler('qotd', qotd))
        dispatcher.add_handler(CommandHandler('start', start))
        dispatcher.add_error_handler(error_callback)


        updater.start_polling()
        print(('{0}||{1}'.format(time.asctime( time.localtime(time.time())), 'Starting polling')))
        updater.idle()


if __name__ == "__main__":
     if not os.path.isdir('misc'):
        try:
            os.mkdir('misc')
        except OSError:
            print ("Creation of the directory failed")
     rabotaetlist = shuffle_bag(rabotaetliresplist, 'rabotaetli')
     stickers = shuffle_bag(petrostickers, 'stickers')
     responces = shuffle_bag(responceslist, 'responces')
     fish = shuffle_bag(fishstick, 'fish')
     memes = meme_bag()

     main()
