#!env python3

# Advent of code day 3
#
# curpos is (x,y)
# so "^v" move y up/down
# and "<>" move x l/r

def updatecurpos(curpos, move):
    cp2 = (0,0)
    if move == '^':
        cp2 = (curpos[0], curpos[1]+1)
    elif move == 'v':
        cp2 = (curpos[0], curpos[1]-1)
    elif move == '<':
        cp2 = (curpos[0]-1, curpos[1])
    elif move == '>':
        cp2 = (curpos[0]+1, curpos[1])
    else:
        raise ValueError('Invalid move: %c', move)
    return(cp2)

def process_a():
    curpos = (0,0)
    moves = 0
    visits = set()
    with open('input.txt') as infile:
        visits.add(curpos)
        while True:
            ch = infile.read(1)
            if not ch:
                break
            else:
                # print("Move from ", curpos, "with direction", ch, end='')
                moves += 1
                curpos = updatecurpos(curpos,ch)
                # print(" to", curpos)
                visits.add(curpos)
    print("Total moves: ", moves)
    print("Final pos:   ", curpos)
    print("Ttl visits:  ",len(visits))

def process_b():
    santapos = (0,0)
    robo_pos = (0,0)
    visits = set()
    with open('input.txt') as infile:
        visits.add(santapos)
        # no need to add initial robopos as it's the same
        while True:
            sp = infile.read(1) # get Santa instruction
            rp = infile.read(1) # get robot instruction
            if not sp:
                break
            else:
                santapos = updatecurpos(santapos, sp)
                robo_pos = updatecurpos(robo_pos, rp)
                visits.add(santapos)
                visits.add(robo_pos)
    print("Houses with at least one present: ", len(visits))

def process():
    process_a()
    process_b()
   
if __name__ == "__main__":
    process()
