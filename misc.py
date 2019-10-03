import csv
import os
import _pickle as pickle
import random
import time
import json
from os import listdir
from os.path import isfile, join


def log(text):
    print(f'{time.asctime( time.localtime(time.time()))}, {text}')


class meme_bag:
    def list_memes(self):
        memes = [f for f in listdir(join(os.path.dirname(os.path.realpath(__file__)),'memes')) if isfile(join(os.path.dirname(os.path.realpath(__file__)),'memes', f))]
        memesToStatus = {i : True for i in memes}
        with open((join(os.path.dirname(os.path.realpath(__file__)), 'misc', 'memes.json')),'w') as f:
            json.dump(memesToStatus, f, ensure_ascii=False, indent=4, separators=(',',': '))
    def __init__(self):
        self.list_memes()
        self.memes =  shuffle_bag('memes')
    def pop(self):
        return join('memes', self.memes.pop())


class shuffle_bag:

    def __init__(self, sourceFile):
        self.source = sourceFile + '.json'
        try:
            with open((join(os.path.dirname(os.path.realpath(__file__)), 'misc', self.source)),'r') as f:
                self.items = json.load(f)
            self.created = True
        except OSError as e:
            log(f'File {sourceFile} not found in folder misc or folder misc wasnt found')
            self.created = False
        except Exception as e:
            print(e)
            self.created = False

    def draw(self):
        result = []
        for item in self.items.keys():
            if self.items[item] == True:
                result.append(item)
        random.shuffle(result)
        return result[-1]


    def refresh(self):
        for item in self.items:
            self.items[item] = True

    def needRefresh(self):
        iter = 0
        for item in self.items:
            if (self.items[item] == False):
                iter += 1
        if iter == len(self.items):
            return True
        else:
            return False

    def pop(self):
        if self.created:
            if self.needRefresh():
                self.refresh()
            item = self.draw()
            self.items[item] = False
            with open((join(os.path.dirname(os.path.realpath(__file__)), 'misc', self.source)),'w') as f:
                json.dump(self.items, f, ensure_ascii=False, indent=4, separators=(',',': '))
            return item
        else:
            log(f'The shuffle bag from {self.source} wasnt created so popping from it is impossible, please fix the filepaths or add the json sources')




if __name__ == "__main__":
    alice = shuffle_bag('petrostickers')
    print(alice.pop())
    log("yes")
    bob = meme_bag()
    print(bob.pop())
     
