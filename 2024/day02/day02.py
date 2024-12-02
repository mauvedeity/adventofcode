#!env python3 

def checkLine(idat):
    if(idat[0] > idat[1]):
        chkvals = [1,2,3]
    else:
        chkvals = [-1,-2,-3]
    thisRepSafe = True
    for i in range(0, len(idat)-1):
        x = idat[i]
        y = idat[i+1]
        thisRepSafe = thisRepSafe and ((x - y) in chkvals)
    return(thisRepSafe)

def process_a(pstrfname = 'input.txt'):
    with open(pstrfname, 'rt') as input:
        safeReps = 0
        for iline in input:
            ida1 = iline.strip().split(' ')
            idat = list(map(int, ida1))
            if checkLine(idat):
                safeReps += 1
    return(safeReps)

def process_b(pstrfname = 'input.txt'):
    with open(pstrfname, 'rt') as input:
        safeReps = 0
        for iline in input:
            ida1 = iline.strip().split(' ')
            idat = list(map(int, ida1))
            if checkLine(idat):
                safeReps += 1
            else:
                thisRepSafe = False
                for i in range(0, len(idat)):
                    tlist = idat.copy()
                    tlist.pop(i)
                    thisRepSafe = thisRepSafe or checkLine(tlist)
                if thisRepSafe:
                    safeReps += 1
    return(safeReps)

def process():
    print(process_a('input.txt'))
    print(process_b('input.txt'))

if __name__ == "__main__":
    process()
