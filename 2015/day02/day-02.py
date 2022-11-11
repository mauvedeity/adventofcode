#!env python3

def wrapsize(l, w, h):  # sorted in order of size!
    side1 = 2 * l * w
    side2 = 2 * w * h
    side3 = 2 * h * l
    slack = l * w
    return(side1 + side2 + side3 + slack)

def ribbonsize(l,w,h):
    run1 = l+l+w+w
    run2 = l*w*h
    return(run1 + run2)
    
def process_a():
    totalwrap = 0
    totalribbon = 0
    with open('input.txt') as inf:
        for line in inf:
            l2 = line[:-1].split('x')
            dims=[int(n) for n in l2]
            dims.sort()
            thiswrap = wrapsize(dims[0], dims[1], dims[2])
            thisribbon = ribbonsize(dims[0], dims[1], dims[2])
            totalwrap += thiswrap
            totalribbon += thisribbon
    print("Total wrapping: ",totalwrap)
    print("Total ribbon: ",totalribbon)

def process():
    process_a()

if __name__ == "__main__":
    process()
