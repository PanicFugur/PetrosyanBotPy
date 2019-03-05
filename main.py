import telegram
from telegram.ext import Updater, CommandHandler
import logging


def shutka(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Ну и шутка, пес!")


updater = Updater(token="431555955:AAHmmmcJM2wcbJBlv7MbpaGVrAAVPgua6Pg")
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
shutka_handler = CommandHandler('shutka', shutka)
dispatcher.add_handler(shutka_handler)
updater.start_polling()