#!/usr/bin/python3
#
# day1b.py
# 
# read measurements, show which have increased or decreased
#

def init_t():
    return(0,0,0)

def rotatein(t1, v):
    tl = list(t1)
    tl.append(v)
    t2 = tuple(tl[1:])
    return(t2)

increased = 0
data = init_t()

fp = open('input.txt', 'rt')
# get first 3 lines
data = rotatein(data, int(fp.readline()))
print(data)
data = rotatein(data, int(fp.readline()))
print(data)
data = rotatein(data, int(fp.readline()))
print(data)
prev = sum(data)
# loop through rest of file
while(True):
    line = fp.readline()
    if("" == line):
        break
    data = rotatein(data, int(line))
    if(sum(data) > prev):
        increased += 1
    prev = sum(data)

print('***\n',increased,'\n***')

## increased = 0
## with open('input.txt', 'rt') as fp:
#    # prev = -1
#    # for l in fp:
#        # curr = int(l)
#        # # is this the first record?
#        # if(prev == -1):
#            # print(curr, 'no previous measurement')
#        # elif(curr > prev):
#            # print(curr, 'increased')
#            # increased += 1
#        # elif(curr < prev):
#            # print(curr, 'decreased')
#        # elif(curr == prev):
#            # print(curr, 'unchanged')
#        # prev = curr
## 
## print('***\n',increased,'\n***')
