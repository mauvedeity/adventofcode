#!env python3
import copy

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
    ltmp = str.strip(copy.copy(line))
    target = 1
    while(len(ltmp)>12):
        if (ltmp.find(str(target)) == -1):
            target += 1
        ltmp = ltmp.replace(str(target),'',1)
    print(ltmp, len(ltmp))
    return(int(ltmp))

def process_b(inputfile):
    result = 0
    with open(inputfile, 'rt') as lines:
        for line in lines:
            result += processlineb(line)
    return(result)

def process():
    print(process_a('input.txt'))
    print(process_b('input-test.txt'))

if __name__ == "__main__":
    process()
