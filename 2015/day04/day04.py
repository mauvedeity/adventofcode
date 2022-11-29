#!env python3
#
# Advent of code day 4
#
# 
import hashlib

def hashOK(testhash):
    return(testhash[:5] == '00000')

def hashOK6(testhash):
    return(testhash[:6] == '000000')

def test():
    test1a = 'abcdef'
    test1b = 609043
    test1s = test1a+str(test1b)
    test1r = hashlib.md5(test1s.encode())
    test1t = test1r.hexdigest()
    print("Test: ", hashOK(test1t))

def process_a():
    mined = False
    # puzzle = 'abcdef'
    # puzzle = 'pqrstuv'
    puzzle = 'yzbqklnj'
    answer = 0
    while not mined:
        acoin = puzzle + str(answer)
        hasha = hashlib.md5(acoin.encode())
        hashb = hasha.hexdigest()
        mined = mined or hashOK(hashb)
        if mined:
            break
        answer = answer + 1
    print("Part 1:")
    print("Value is:   ", answer)
    print("Hash value: ", hashb)
    return

def process_b():
    mined = False
    puzzle = 'yzbqklnj'
    answer = 282748
    while not mined:
        acoin = puzzle + str(answer)
        hasha = hashlib.md5(acoin.encode())
        hashb = hasha.hexdigest()
        mined = mined or hashOK6(hashb)
        if mined:
            break
        answer = answer + 1
    print("Part 2:")
    print("Value is:   ", answer)
    print("Hash value: ", hashb)
    return

def process():
    # test()
    process_a()
    process_b()
   
if __name__ == "__main__":
    process()
