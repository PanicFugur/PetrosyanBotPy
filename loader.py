import json


def loadFileToJSON(filename):
    result = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                result.update({line[:-1] : True})
        with open('misc/quotes.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4,  separators=(',',': '))
    except Exception as e:
        print(e)
 
if __name__ == "__main__":
    loadFileToJSON('source.txt')