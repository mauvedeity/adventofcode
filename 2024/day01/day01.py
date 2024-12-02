#!env python3 

def process_a():
    with open('input.txt', 'r') as inputf:
        left=[]
        rght=[]
        for line in inputf:
            sl = line.split()
            left.append(int(sl[0]))
            rght.append(int(sl[1]))

    left.sort()
    rght.sort()
    dist = 0
    ll = len(left)
    for iptr in range(0, ll):
        sep = abs(left[iptr] - rght[iptr])
        dist += sep

    print('Total distance: ', dist)
    return

def num_hits(pint, plist):
    matches = 0
    for iptr in plist:
        if iptr == pint:
            matches += 1
    return(matches)


def process_b():
    with open('input.txt', 'r') as inputf:
        left=[]
        rght=[]
        for line in inputf:
            sl = line.split()
            left.append(int(sl[0]))
            rght.append(int(sl[1]))

    simscore = 0
    for iptr in left:
        linescore = (iptr * num_hits(iptr, rght))
        simscore += linescore

    print('Similarity score: ', simscore)

    return

def process():
    process_a()
    process_b()

if __name__ == "__main__":
    process()
