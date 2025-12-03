#!env python3

def validateid(intid):
    id = str(intid)
    valid = True
    idlen = len(id)
    if((idlen % 2) == 0):       # even number of digits
        split = int(idlen / 2)
        h1 = id[:split]
        h2 = id[split:]
        if (h1 == h2):
            valid = False
    return(valid)

def validaterange(start, finish):
    sum_invalid = 0
    intstart = int(start)
    intfinish = int(finish) + 1
    for id in range(intstart, intfinish):
        if not validateid(id):
            sum_invalid += id
    return(sum_invalid)

def reparserange(rangestr):
    l = rangestr.split('-')
    lo = l[0]
    hi = l[1]
    return(validaterange(lo, hi))

def process_a(inputfile):
    result = 0
    with open(inputfile, 'rt') as inf:
        data = inf.readline()
        dlist = data.split(',')
        for d in dlist:
            result += reparserange(d)
    return(result)

def process_b(inputfile):
    return(0)

def process():
    print(process_a('input.txt'))
    print(process_b('input-test.txt'))

if __name__ == "__main__":
    process()
