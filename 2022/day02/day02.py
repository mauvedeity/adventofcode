#!env python3 

def shapescore(ashape):
    if ashape == 'X':
        return(1)
    elif ashape == 'Y':
        return(2)
    elif ashape == 'Z':
        return(3)
    else:
        raise(ValueError)

# score a round
# 0 for a loss, 3 for a draw, 6 if won
#
def roundscore(opmove, mymove):
    rv = 0
    if(ord(opmove) == ord(mymove)-23):   # draw
        rv = 3
    if((opmove == 'A') and (mymove == 'Y')):
        rv = 6        
    elif((opmove == 'B') and (mymove == 'Z')):
        rv = 6
    elif((opmove == 'C') and (mymove == 'X')):
        rv = 6
    return(rv)

def score_a(opmove, mymove):
    score = 0
    score += shapescore(mymove)
    score += roundscore(opmove, mymove)
    return(score)

def process_a():
    score = 0
    with open('input.txt') as infile:
        for li in infile:
            li = li.strip()
            om = li[0]
            mm = li[2]
            score += score_a(om, mm)
            # print(om, mm, score_a(om, mm))
        print("Total score: ", score)
    return

def process_b():
    return

def process():
    process_a()
    process_b()

if __name__ == "__main__":
    process()