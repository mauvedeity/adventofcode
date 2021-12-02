#!/usr/bin/python3
#
# day2b.py
#

with open('input.txt') as fp:
    forward = 0
    depth = 0
    aim = 0
    for ln in fp:
        cmd, dist = ln.split(' ')
        # cmd is one of 'down', 'forward', 'up'
        if(cmd == 'down'):
            # depth += int(dist)
            aim += int(dist)
        elif(cmd == 'up'):
            # depth -= int(dist)
            aim -= int(dist)
        elif(cmd == 'forward'):
            # forward += int(dist)
            forward += int(dist)
            depth += aim * int(dist)
        else:
            print('Bad command')
            exit()

print('Forward:', forward, '\nDepth:', depth, '\nResult:', depth*forward)

