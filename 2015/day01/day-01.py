#!env python3

def process_a():
    # open file
    floor = 0
    chars = 0
    achar = ''
    basement_visited = False
    with open('day01-a-input.txt', 'rt') as inf:
        while True:
            achar = inf.read(1)
            if not achar:
                break
            chars += 1
            if(achar == '('):
                floor += 1
            else:
                floor -= 1
            if((floor == -1) and not basement_visited):
                print("First basement visit: ", chars)
                basement_visited = True

    print("Characters read: ", chars)
    print("Floor reached:   ", floor)      

if __name__ == "__main__":
    process_a()
