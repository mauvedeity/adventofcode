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

def validate2(intid):
    valid = True
    strid = str(intid)
    slen = len(strid)
    hslen = int(slen/2)
    for seg in range(1, hslen+1):
        sseg = strid[0:seg]
        for lens in range(1, 10):
            tstr = sseg*lens
            if(tstr == strid):
                return(False)
    return(valid)

def validater2(start, finish):
    sum_invalid = 0
    intstart = int(start)
    intfinish = int(finish) + 1
    for id in range(intstart, intfinish):
        if not validate2(id):
            sum_invalid += id
    return(sum_invalid)

def reparse2(rangestr):
    l = rangestr.split('-')
    lo, hi = l[0], l[1]
    return(validater2(lo, hi))

def process_a(inputfile):
    result = 0
    with open(inputfile, 'rt') as inf:
        data = inf.readline()
        dlist = data.split(',')
        for d in dlist:
            result += reparserange(d)
    return(result)

def process_b(inputfile):
    result = 0
    with open(inputfile, 'rt') as inf:
        data = inf.readline()
        dlist = data.split(',')
        for d in dlist:
            print (d)
            result += reparse2(d)
    return(result)

def process():
    print(process_a('input.txt'))
    print(process_b('input.txt'))

if __name__ == "__main__":
    process()
