import telegram
from telegram.ext import Updater, CommandHandler
import logging
import random
from responces import rabotaetliresplist, version, petrostickers, responceslist, fishstick, quotes
from misc import load_file, shuffle_bag

rabotaetlist = shuffle_bag(rabotaetliresplist)
stickers = shuffle_bag(petrostickers)
responces = shuffle_bag(responceslist)
fish = shuffle_bag(fishstick)

def rabotaetli(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=rabotaetlist.pop())


def ver(bot, update):
   bot.send_message(chat_id=update.message.chat_id, text=version) 


def shutka(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=responces.pop())
    for x in range(5):
        bot.send_sticker(chat_id=update.message.chat_id,
                         sticker=stickers.pop())


def neznayu(bot, update):
    for x in range(5):
        bot.send_sticker(chat_id=update.message.chat_id,
                         sticker=fish.pop())


def nebo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='А где неба нет?')
    bot.send_sticker(chat_id=update.message.chat_id,
                     sticker=petrostickers[-1])


def topshutka(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text='https://www.youtube.com/watch?v=VQGLnaNQKds')


def mem(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text='Здесь должен быть мем, но увы их нет, ибо создатель пес')



updater = Updater(token="431555955:AAHvMcpo42jf-TFeDvsTEeJ2yZCN0X5Jmjs") #Account for faulty token
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
rabotaetli_handler = CommandHandler('rabotaetli', rabotaetli) #Make loading smarter, like a list or something, it's an eyesore
ver_handler = CommandHandler('ver', ver)
shutka_handler = CommandHandler('shutka', shutka)
fish_handler = CommandHandler('fish', neznayu)
nebo_handler = CommandHandler('nebo', nebo)
topshutka_handler = CommandHandler('topshutka', topshutka)
dispatcher.add_handler(rabotaetli_handler)
dispatcher.add_handler(ver_handler)
dispatcher.add_handler(shutka_handler)
dispatcher.add_handler(fish_handler)
dispatcher.add_handler(nebo_handler)
dispatcher.add_handler(topshutka_handler)
updater.start_polling()