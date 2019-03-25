# - *- coding: utf- 8 - *-
import os
import _pickle as pickle
import random
import time
import logging

from misc import shuffle_bag
from responces import quotes
from os.path import join

def main():
    try:
        with open(join(os.path.dirname(os.path.realpath(__file__)),'qotd'), 'rb') as f:
            print(pickle.load(f))
        logging.basicConfig(filename=join(os.path.dirname(os.path.realpath(__file__)),'app.log'), format='%(asctime)s - %(message)s', level=logging.INFO)
        qoutelist = shuffle_bag(quotes, 'qotd')
        qotd = qoutelist.pop()
        with open(join(os.path.dirname(os.path.realpath(__file__)),'qotd'), 'wb') as f:
            pickle.dump(qotd, f)
        logging.info('Quote changed')
        with open(join(os.path.dirname(os.path.realpath(__file__)),'qotd'), 'rb') as f:
            print(pickle.load(f))
    except FileNotFoundError:
        with open(join(os.path.dirname(os.path.realpath(__file__)),'qotd'), 'wb') as f:
            print("File wasn't found and created")
            main()
    except Exception as e:
        print('Error had occured while picking a quote')
        print(e)
        logging.info('Error had occured while picking a quote')
        logging.info(e)

if __name__ == "__main__":
    main()
    

   
