#!env python3 

import re

def do_mul(pinstr):
    # 'mul(ddd,ddd)'
    lop,rop = pinstr.split(',')
    lop = lop[4:]
    rop = rop[:-1]
    return(int(lop) * int(rop))

def process_a(pstrfname = 'input.txt'):
    SEARCH = r'mul\(\d+,\d+\)'
    result = 0
    with open(pstrfname, 'rt') as infile:
        for i in infile:
            m1 = re.findall(SEARCH, i)
            m2 = sum(list(map(do_mul, m1)))
            result += m2
    return(result)

def process_b(pstrfname = 'input.txt'):
    return

def process():
    print(process_a('input.txt'))
    print(process_b('input-1.txt'))

if __name__ == "__main__":
    process()
