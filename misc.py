import csv
import os
import _pickle as pickle
import random
import time
from os import listdir
from os.path import isfile, join


class shuffle_bag:

    def __init__(self, items, ffile):
        if (isfile(join('misc', ffile))) and (os.path.getsize(join(os.path.dirname(os.path.realpath(__file__)),'misc', ffile)) > 0):
            with open((join(os.path.dirname(os.path.realpath(__file__)), 'misc', ffile)),'rb') as f:
                self.items = pickle.load(f)
                print('{0}||{1} file found and loaded data from it'.format(time.asctime( time.localtime(time.time())),ffile))
        else:
            if not isfile(join(os.path.dirname(os.path.realpath(__file__)),'misc', ffile)):
                a = open(join(os.path.dirname(os.path.realpath(__file__)),'misc', ffile), 'wb')
                a.close()
                print('{0}||{1} file not found, creating'.format(time.asctime( time.localtime(time.time())) ,ffile))
            else:
                print('{0}||{1} file is found but is empty'.format(time.asctime( time.localtime(time.time())) ,ffile))
            self.items = items.copy()
        self.source = items.copy()
        self.file = ffile

    def draw(self):
        random.shuffle(self.items)
        picked_item = self.items[-1]
        self.items.pop(-1)
        with open(join(os.path.dirname(os.path.realpath(__file__)),'misc', self.file), 'wb') as f:
            pickle.dump(self.items, f)
        return picked_item

    def pop(self):
        try:
            if self.items:
                result = self.draw()
            else:
                self.items = self.source.copy()
                result = self.draw()
        except:
            print(('{0}||{1}: {2}'.format(time.asctime( time.localtime(time.time())), 'Error popping from', self.file)))
        return result


class meme_bag:
    def list_memes(self):
        memes = [f for f in listdir(join(os.path.dirname(os.path.realpath(__file__)),'memes')) if isfile(join(os.path.dirname(os.path.realpath(__file__)),'memes', f))]
        return memes
    def __init__(self):
        self.memes =  shuffle_bag(self.list_memes(), 'memes')
    def pop(self):
        return join('memes', self.memes.pop())
