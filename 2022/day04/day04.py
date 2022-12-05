#!env python3 

def is_contained(pl1, pr1, pl2, pr2):
    contains = False
    set1 = set(range(int(pl1), int(pr1)+1))
    set2 = set(range(int(pl2), int(pr2)+1))
    contains = contains or set1.issubset(set2)
    contains = contains or set2.issubset(set1)
    return(contains)

def is_overlap(pl1, pr1, pl2, pr2):
    overlaps = False
    l1 = list(range(int(pl1), int(pr1)+1))
    l2 = list(range(int(pl2), int(pr2)+1))
    print(l1)
    print(l2)
    for lidx in l1:
        if lidx in l2:
            overlaps = True
            break
    return(overlaps)

def process_a():
    contains = 0
    with open('input.txt') as infile:
        for li in infile:
            li = li.strip()
            l1, r1, l2, r2 = li.replace('-',',').split(',')
            if is_contained(l1,r1,l2,r2):
                contains += 1

    print("Fully contained sets: ", contains)
    return

def process_b():
    overlaps = 0
    with open('input.txt') as infile:
        for li in infile:
            li = li.strip()
            l1, r1, l2, r2 = li.replace('-',',').split(',')
            if is_overlap(l1,r1,l2,r2):
                overlaps += 1
                # print(l1,r1,l2,r2)
    print("Overlapping sets: ", overlaps)
    return

def process():
    process_a()
    process_b()

if __name__ == "__main__":
    process()
