#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import random
import time
from os.path import join

import telegram
from telegram.ext import CommandHandler, Updater

#from handlers import rabotaetli, ver, shutka, neznayu, nebo, topshutka, mem, qotd, start
import _pickle as pickle
import handlers
import securestuff
from err import error_callback
from misc import shuffle_bag


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

        dispatcher.add_handler(CommandHandler('rabotaetli', handlers.rabotaetli))
        dispatcher.add_handler(CommandHandler('qotd', handlers.qotd))
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

     main()
