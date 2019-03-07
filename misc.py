import csv
import random
from os import listdir
from os.path import isfile, join


def load_file(filename):
    file = open(filename, 'r')
    reader = csv.reader(file)
    allRows = [row for row in reader]
    return allRows
    

class shuffle_bag:

    def __init__(self, items):
        self.items = items.copy()
        self.source = self.items.copy()

    def draw(self):
        random.shuffle(self.items)
        picked_item = self.items[-1]
        self.items.pop(-1)
        return picked_item

    def pop(self):
        if self.items:
            result = self.draw()
        else:
            self.items = self.source.copy()
            result = self.draw()
        return result


class meme_bag:
    def list_memes(self):
        memes = [f for f in listdir('memes') if isfile(join('memes', f))]
        return memes
    def __init__(self):
        self.memes =  shuffle_bag(self.list_memes())
    def pop(self):
        return join('memes', self.memes.pop())



