import schedule
import time
import pickle
import os
from responces import quotes
from misc import shuffle_bag


qoutelist = shuffle_bag(quotes)

def pick():
    qotd = qoutelist.pop()
    with open('qotd.txt', 'wb') as f:
        pickle.dump(qotd, f)
    print('Quote changed')    

schedule.every().day.at("21:01").do(pick)

if os.path.isfile('./qotd.txt'):
         os.remove('qotd.txt')
pick()
while 1:
    schedule.run_pending()
    time.sleep(1)