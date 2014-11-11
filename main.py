__author__ = 'Andrew'

#quick tool to create a functonal javascript array from a raw csv file format
import csv
import sys

csvfile = open('data.csv', 'rt')
reader = csv.reader(csvfile)
for row in reader:
    print ("{City: '" + row[0] + "', Index: " + row[1] + ", LivingIndex: " + row[2] + "},")

