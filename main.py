import telegram
from telegram.ext import Updater, CommandHandler
import logging
import random
from responces import rabotaetliresplist, version, petrostickers
from misc import load_file


def rabotaetli(bot, update):
    number = random.randrange(0,3)
    bot.send_message(chat_id=update.message.chat_id, text=rabotaetliresplist[number])


def ver(bot, update):
   bot.send_message(chat_id=update.message.chat_id, text=version) 


def shutka(bot, update):
    stickers = load_file("Stickers.txt")
    responces = load_file("Responces.txt")
    random.shuffle(responces)
    bot.send_message(chat_id=update.message.chat_id, text=responces[0])
    for x in range(5):
        random.shuffle(stickers)
        number = random.randrange(0, len(stickers)-1)
        bot.send_sticker(chat_id=update.message.chat_id,
                         sticker=stickers[number])


def fish(bot, update):
    fish = load_file('Fish.txt')
    for x in range(5):
        random.shuffle(fish)
        number = random.randrange(0, len(fish)-1)
        bot.send_sticker(chat_id=update.message.chat_id,
                         sticker=fish[number])


   


updater = Updater(token="431555955:AAHmmmcJM2wcbJBlv7MbpaGVrAAVPgua6Pg")
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
rabotaetli_handler = CommandHandler('rabotaetli', rabotaetli)
ver_handler = CommandHandler('ver', ver)
shutka_handler = CommandHandler('shutka', shutka)
dispatcher.add_handler(rabotaetli_handler)
dispatcher.add_handler(ver_handler)
dispatcher.add_handler(shutka_handler)
updater.start_polling()