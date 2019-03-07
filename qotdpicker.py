import schedule
import time
import pickle
import os
from responces import quotes
from misc import shuffle_bag


qoutelist = shuffle_bag(quotes)

def pick():
    os.remove('qotd.txt')
    qotd = qoutelist.pop()
    with open('qotd.txt', 'w') as f:
        pickle.dump(qotd, f)

schedule.every().day.at("22:08").do(pick)

while 1:
    schedule.run_pending()
    time.sleep(1)
