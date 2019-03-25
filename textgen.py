from os.path import join
from random import choice
import sys

def openfile(filename):
    try:
        words = []
        with open(filename,'r', encoding='utf8') as f:
            for line in f:
                words.extend(line.split())
        return words
    except FileNotFoundError:
        print("Couldn't find source file")

def makerule(data, context):
    rule = {}
    words = data
    index = context
    for word in words[index:]:
        key = ' '.join(words[index-context:index])
        if key in rule:
            rule[key].append(word)
        else:
            rule[key] = [word]
        index += 1
 
    return rule

def makestring(rule, length):    
    oldwords = choice(list(rule.keys())).split(' ') #random starting words
    string = ' '.join(oldwords) + ' '
 
    for i in range(length):
        try:
            key = ' '.join(oldwords)
            newword = choice(rule[key])
            string += newword + ' '
 
            for word in range(len(oldwords)):
                oldwords[word] = oldwords[(word + 1) % len(oldwords)]
            oldwords[-1] = newword
 
        except KeyError:
            return string
    return string
def getKolyaVbros():
    data = openfile(join('misc', 'Kolyan.txt'))
    rule = makerule(data, 3)
    string = makestring(rule, 30)
    string = string.capitalize()
    string = string.append('.')
    return string

if __name__ == '__main__':
    data = openfile(join('misc', 'Kolyan.txt'))
    rule = makerule(data, 3)
    string = makestring(rule, 30)
    print(string.capitalize())
