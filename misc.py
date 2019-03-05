import csv


def load_file(filename):
    file = open(filename, 'r')
    reader = csv.reader(file)
    allRows = [row for row in reader]
    return allRows
