#!env python3
#
# day01.py
#
# Part 1
def part1(dfile):
    start = 50
    combo = 0
    with open(dfile, 'rt') as inf:
        for i in inf:
            if(len(i) > 1):
                dir = i[0]  
                stp = int(i[1:])
            if(dir == 'L'):
                start = (start - stp) % 100
            else:
                start = (start + stp) % 100
            if(start == 0):
                combo += 1
    return(combo)

# Part 2
def part2(dfile):
    posn = 50
    combo = 0
    with open(dfile, 'rt') as inf:
        for i in inf:
            if(len(i) > 1):
                dir = i[0]
                stp = int(i[1:])
                if(dir == 'L'):
                    for p in range(stp):
                        posn = (posn - 1) % 100
                        if(posn == 0):
                            combo += 1
                else:
                    for p in range(stp):
                        posn = (posn + 1) % 100
                        if(posn == 0):
                            combo += 1
    return(combo)

print('Combo:', part1('input-a.txt'))
print('Combo:', part2('input-a.txt'))
