#!env python3
import copy
import string
from itertools import combinations;

def combine(a, b):
    ia = int(a)
    ib = int(b)
    return((ia * 10) + ib)

def processlinea(line):
    max = 0
    llen = len(line)
    for tptr in range(llen - 1):
        for uptr in range(tptr + 1, llen-1):
            val = combine(line[tptr], line[uptr])
            if (val > max):
                max = val
    return(max)

def process_a(inputfile):
    result = 0
    with open(inputfile, 'rt') as lines:
        for line in lines:
            result += processlinea(line)
    return(result)

def processlineb(line):
    expline = list(line.strip())
    result = 0
    combos = list(combinations(expline,12))
    for combo in combos:
        cv = ''
        for i in combo:
            cv += i
        if(int(cv) > result):
            result = int(cv)
    return(result)

def process_b(inputfile):
    result = 0
    with open(inputfile, 'rt') as lines:
        for line in lines:
            result += processlineb(line)
            print('.', end='')
    return(result)

def process():
    print(process_a('input.txt'))
    print(process_b('input.txt'))

if __name__ == "__main__":
    process()
