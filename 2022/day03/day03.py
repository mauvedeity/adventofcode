#!env python3 

ALLCHRS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def between(ck, lo, hi):
    return((ck >= lo) and (ck <= hi))

def calc_priority(pitem):
    #if len(pitem) > 1:
        #print(len(pitem), pitem)
    if(pitem == ''):
        return 0
    else:
        ordinal = ord(pitem)
        if (between(ordinal, 65,90)):   # uppercase
            priority = ordinal-38
        elif (between(ordinal, 97,122)):
            priority = ordinal-96
        else:
            raise(ValueError)
    return priority

def bifurcate(aline):
    slen = len(aline)
    slen = (int(slen / 2))
    h1 = aline[:slen]
    h2 = aline[slen:]
    return(h1,h2)

def compartments(pcmp1, pcmp2):
    rv = ''
    for chidx in ALLCHRS:
        if ((chidx in pcmp1) and (chidx in pcmp2)):
            rv += chidx
    return(rv)

def process_a():
    prioritysum = 0
    with open('input.txt') as infile:
        for li in infile:
            li = li.strip()
            cmp1, cmp2 = bifurcate(li)
            cmpt = compartments(cmp1, cmp2)
            prioritysum += calc_priority(cmpt)
    print("Priority sum = ", prioritysum)
    return

def groupscan(pl1, pl2, pl3):
    rv = ''
    for chidx in ALLCHRS:
        l1 = chidx in pl1
        if ((chidx in pl1) and (chidx in pl2) and (chidx in pl3)):
            rv = chidx
            break
    return(rv)

def process_b():
    prioritysum = 0
    n = 0
    with open('input.txt') as infile:
        while n <= 100:
            li1 = (infile.readline()).strip()
            li2 = (infile.readline()).strip()
            li3 = (infile.readline()).strip()
            prioritysum += calc_priority(groupscan(li1,li2,li3))
            n += 1
    print("Result: ", prioritysum)
    return

def process():
    process_a()
    process_b()

if __name__ == "__main__":
    process()
