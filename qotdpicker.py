# - *- coding: utf- 8 - *-
import os
import pickle
import random
import time
import logging

from misc import shuffle_bag
from responces import quotes
from os.path import join

try:
    logging.basicConfig(filename=join(os.path.dirname(os.path.realpath(__file__)),'app.log'), format='%(asctime)s - %(message)s', level=logging.INFO)
    qoutelist = shuffle_bag(quotes, 'qotd')
    qotd = qoutelist.pop()
    with open('qotd', 'wb') as f:
        pickle.dump(qotd, f)
    logging.info('Quote changed')
except Exception as e:
    print('Error had occured while picking a quote')
    print(e)
    logging.info('Error had occured while picking a quote')
    logging.info(e)
    

   
