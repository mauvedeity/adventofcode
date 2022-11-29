#!env python3
#
# Advent of Code day 5
#
#
def isvowel(ch):
    return(ch in 'aeiou')

def vowelcount(pstr):
    isnice = False
    vct = 0
    for ch in pstr:
        if(isvowel(ch)):
            vct = vct+1
    return (vct > 2)

def doubleletter(pstr):
    prevch = ''
    isnice = False
    for ch in pstr:
        isnice = isnice or ch == prevch
        prevch = ch
    return isnice

def bannedstrings(pstr):
    isnice = True
    # 'ab' 'cd' 'pq' 'xy'
    isnice = isnice and not('ab' in pstr)
    isnice = isnice and not('cd' in pstr)
    isnice = isnice and not('pq' in pstr)
    isnice = isnice and not('xy' in pstr)
    return isnice

def isnice(pstr):
    return(vowelcount(pstr) and doubleletter(pstr) and bannedstrings(pstr))

def process_a():
    nicect = 0
    naughtyct = 0
    with open('input.txt') as infile:
        for li in infile:
            li = li[:-1]
            if isnice(li):
                nicect += 1
            else:
                naughtyct += 1

    print("Nice count: ", nicect)
    print("Naughty ct: ", naughtyct)

def haspairx2(pstr):
    isnice = False
    idx = len(pstr)-1
    for i in range(0,idx):
        # print(pstr, pstr[i], pstr[i+1])
        chch1 = pstr[i:i+2]
        for i2 in range(i+2, idx):
            chch2 = pstr[i2:i2+2]
            # print("D: ",chch1, chch2)
            if(chch1 == chch2):
                isnice = True
                break
    return isnice

def separatedrepeat(pstr):
    isnice = False
    idx = len(pstr)-2
    for i in range(0,idx):
        if(pstr[i] == pstr[i+2]):
            isnice = True
            break
    return isnice

def isnice2(pstr):
    return(haspairx2(pstr) and separatedrepeat(pstr))

def process_b():
    nicect = 0
    naughtyct = 0
    with open('input.txt') as infile:
        for li in infile:
            li = li.strip()
            # print(li, isnice2(li), haspairx2(li), separatedrepeat(li))
            if isnice2(li):
                nicect += 1
            else:
                naughtyct += 1

    print("Nice count: ", nicect)
    print("Naughty ct: ", naughtyct)

def process():
    # process_a()
    process_b()
   
if __name__ == "__main__":
    process()
