import telegram
from telegram.ext import Updater, CommandHandler
import logging
import random
from responces import rabotaetliresplist

def rabotaetli(bot, update):
    number = random.randrange(0,2)
    bot.send_message(chat_id=update.message.chat_id, text=rabotaetliresplist[number])




updater = Updater(token="431555955:AAHmmmcJM2wcbJBlv7MbpaGVrAAVPgua6Pg")
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
rabotaetli_handler = CommandHandler('rabotaetli', rabotaetli)
dispatcher.add_handler(rabotaetli_handler)
updater.start_polling()