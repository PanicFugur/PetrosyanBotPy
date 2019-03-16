import os
import pickle
import random
import time
import logging

from misc import shuffle_bag
from responces import quotes

logging.basicConfig(filename='misc/app.log', format='%(asctime)s - %(message)s', level=logging.INFO)
qoutelist = shuffle_bag(quotes, 'qotd')
qotd = qoutelist.pop()
with open('qotd', 'wb') as f:
    pickle.dump(qotd, f)
logging.info('Quote changed')
   
