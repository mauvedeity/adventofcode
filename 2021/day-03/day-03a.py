#!/usr/bin/python3
#
# day 3 part 1
#

# [0,0,0,0,0,0,0,0,0,0,0,0]

def adder(curr, this):
    for i in range(len(curr)):
        curr[i] += int(this[i])
    return(curr)

def getbitcounts():
    with open('input.txt') as fp:
        l = [0,0,0,0,0,0,0,0,0,0,0,0]
        lines = 0
        for ln in fp:
            line = list(ln)
            l = adder(l, line)
            lines += 1
    return(l, lines)

def processbitcounts():
    vector, lines = getbitcounts()
    l2 = lines / 2
    vl = len(vector)
    gamma = ''
    epsilon = ''
    for i in range(vl):
        if(vector[i]>l2):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return(gamma, epsilon)

def main():
    gamma, epsilon = processbitcounts()
    g2 = int(gamma, 2)
    e2 = int(epsilon, 2)
    print(g2, e2, g2*e2)

if __name__ == "__main__":
    main()

