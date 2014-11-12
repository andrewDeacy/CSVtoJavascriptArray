__author__ = 'Andrew'
#quick tool to create a functional javascript array from a raw csv file format
import csv
import sys

isValid = 0
columns = []

while isValid < 1:
    try:
        number = input('Enter the amount of columns in the array: ')
        if int(number) > 0:
            for num in range(0,int(number)):
                name = input('Enter the name for each column: ')
                columns.append(name)
                isValid = 2
        else:
            isValid = 0
    except:
        print ('Error enter a valid number please...')
isValid = 0

length = int(len(columns))

while isValid < 1:
    csvfile = open('data.csv', 'rt')
    reader = csv.reader(csvfile)

    for row in reader:
        print('{', end="")
        #need to find out if row is a int or string to determine if i need quotes

        for num in range(0, length):
            if isinstance(row[num], float):
                if (num) == (length -1):
                    print (columns[num] + ": " + row[num], end="")
                else:
                    print (columns[num] + ": " + row[num], end="")
            else:
                if (num) == (length -1):
                    print (columns[num] + ": " "'" + row[num] + "'", end="")
                else:
                    print (columns[num] + ": " "'" + row[num] + "',", end="")
        print('}')
