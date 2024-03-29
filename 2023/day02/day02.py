#!env python3 

def getgameno(pstr):
    data = pstr.split(":")[0]
    data = data.replace('Game ','')
    return(int(data))

def ispossible(pred, pgreen, pblue):
    return((pred <= 12) and (pgreen <= 13) and (pblue <= 14))

def process_a(pdatafile):
    rv = 0
    gameno = 0
    with open(pdatafile) as infile:
        for li in infile:
            gameno = getgameno(li)
            possible = True
            for agame in li.split(":")[1].split(";"):
                red, green, blue = 0,0,0
                for l3 in agame.split(','):
                    kount = int((l3.strip().split(' ')[0]))
                    color = ((l3.strip().split(' ')[1]))
                    if(color == 'red'):
                        red += kount
                    elif(color == 'green'):
                        green += kount
                    else:
                        blue += kount
                    possible = possible and ispossible(red, green, blue)
            if(possible):
                # print(gameno)
                rv += gameno
    return(rv)

def process_b(pdatafile):
    rv = 0
    gameno = 0
    powers = 0
    with open(pdatafile) as infile:
        for li in infile:
            gameno = getgameno(li)
            red, green, blue = 1,1,1
            for agame in li.split(":")[1].split(";"):
                for l3 in agame.split(','):
                    kount = int((l3.strip().split(' ')[0]))
                    color = ((l3.strip().split(' ')[1]))
                    if(color == 'red'):
                        red = max(kount, red)
                    elif(color == 'green'):
                        green = max(kount, green)
                    else:
                        blue = max(blue, kount)
            thisgame = (red * green * blue)
            powers += thisgame
    return(powers)

def process():
    print("Part A: ", process_a('input.txt'));
    print("Part B: ", process_b('input.txt'));

if __name__ == "__main__":
    process()
