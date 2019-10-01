import csv
import os
import _pickle as pickle
import random
import time
import json
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


class shuffle_bag2:
    # def __init__(self, sourceFile):
    #     #need to follow the ask forgiveness not permission principle
    #     self.source = sourceFile
    #     if not os.path.isdir('misc'):
    #         os.mkdir('misc')
    #     if not (isfile(os.path.join('misc', sourceFile))):
    #         print('The file doesnt exist')
    #     if os.path.isdir('misc') and os.path.isfile(os.path.join('misc', sourceFile)):
    #         with open((join(os.path.dirname(os.path.realpath(__file__)), 'misc', self.source)),'r') as f:
    #             self.items = json.load(f)

    def __init__(self, sourceFile):
        self.source = sourceFile
        try:
            with open((join(os.path.dirname(os.path.realpath(__file__)), 'misc', self.source)),'r') as f:
                self.items = json.load(f)
        except OSError as e:
            print(e)
        except Exception as e:
            print(e)





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
        if self.needRefresh():
            self.refresh()
        item = self.draw()
        self.items[item] = False
        with open((join(os.path.dirname(os.path.realpath(__file__)), 'misc', self.source)),'w') as f:
            json.dump(self.items, f, ensure_ascii=False, indent=4, separators=(',',': '))
        return item


if __name__ == "__main__":
    a = shuffle_bag2('petrosticker.json')
    print(a.pop())
