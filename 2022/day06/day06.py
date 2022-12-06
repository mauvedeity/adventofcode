#!env python3 
#
# Day 06
#

def ismarker(pmrk):
    return(len(set(pmrk)) == len(pmrk))

def scan_a(pli,pmrksz):
    for idx in range((pmrksz), len(pli)):
        if ismarker(pli[idx-pmrksz:idx]):
            return idx

def process_a():
    with open('inputx.txt') as infile:
        for li in infile:
            li = li.strip()
            markerpos = scan_a(li,4)
            print("Marker at: ", markerpos)
    return

def process_b():
    with open('input.txt') as infile:
        for li in infile:
            li = li.strip()
            markerpos = scan_a(li,14)
            print("Marker at: ", markerpos)
    return

def process():
    # process_a()
    process_b()

if __name__ == "__main__":
    process()
