#!env python3 

# digits = [('one','1'), ('two','2'), ('three','3'), ('four','4'), ('five','5'), ('six','6'), ('seven','7'), ('eight','8'), ('nine','9')];

digits = [
    ("one", "o1e"),
    ("two", "t2"),
    ("three", "t3e"),
    ("four", "4"),
    ("five", "5e"),
    ("six", "6"),
    ("seven", "7n"),
    ("eight", "e8t"),
    ("nine", "n9e")
]

def getfirstnum(pstr):
    for pc in pstr:
        if (pc.isdigit()):
            return(int(pc))
        
def getlastnum(pstr):
    rv = ''
    for pc in pstr:
        if(pc.isdigit()):
            rv = pc
    return(int(rv))

def numreplace(pstr):
    rv = pstr.strip()
    for d in digits:
        rv = rv.replace(d[0], d[1])
    print(rv)
    return(rv)

def process_a():
    total = 0
    with open('input.txt') as infile:
        for li in infile:
            sum = (getfirstnum(li) * 10) + getlastnum(li)
            total += sum
    print("Part 1:", total)

#  one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

def process_b():
    total = 0
    with open('input.txt') as infile:
        for li in infile:
            li2 = numreplace(li)
            sum = (getfirstnum(li2) * 10) + getlastnum(li2)
            # print(li,li2,sum)
            total += sum
    print("Part 2:", total)
    return

def process():
    process_a()
    process_b()

if __name__ == "__main__":
    process()
