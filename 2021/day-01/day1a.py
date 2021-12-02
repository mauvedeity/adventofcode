#!/usr/bin/python3
#
# day1.py
# 
# read measurements, show which have increased or decreased
#
increased = 0
with open('input.txt', 'rt') as fp:
    prev = -1
    for l in fp:
        curr = int(l)
        # is this the first record?
        if(prev == -1):
            print(curr, 'no previous measurement')
        elif(curr > prev):
            print(curr, 'increased')
            increased += 1
        elif(curr < prev):
            print(curr, 'decreased')
        elif(curr == prev):
            print(curr, 'unchanged')
        prev = curr

print('***\n',increased,'\n***')
