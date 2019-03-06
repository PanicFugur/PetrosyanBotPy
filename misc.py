import csv
import random


def load_file(filename):
    file = open(filename, 'r')
    reader = csv.reader(file)
    allRows = [row for row in reader]
    return allRows


class shuffle_bag:

    def __init__(self, items):
        self.items = items
        self.source = items

    def refill(func):
        def wrapper(self):
            if len(self.items) == 0:
                self.items = self.source
                func(self)
            else:
                func(self)
        return wrapper

    @refill
    def pop(self):
        random.shuffle(self.items)
        picked_item = self.items[len(self.items)-1]
        self.items.pop(len(self.items)-1)
        return picked_item
