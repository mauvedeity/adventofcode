#!env python3 

from anytree import Node, RenderTree

# / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)

#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)

def do_test():
    fsroot = Node('',fsize=0)
    adir = Node('a', fsize=0, parent = fsroot)
    edir = Node('e', fsize=0, parent = fsroot)
    ifile = Node('i', fsize=584, parent = edir)
    ffile = Node('f', fsize=29116,parent = fsroot)
    gfile = Node('g', fsize=2557,parent = fsroot)
    hfile = Node('h.lst', fsize=62596)

    bfile = Node('b.txt', fsize=14848514, parent = fsroot)
    cfile = Node('c.dat', fsize= 8504156, parent = fsroot)

    ddir = Node('d', fsize=0, parent = fsroot)

    jfile = Node('k', fsize=4060174, parent = ddir)
    dfil2 = Node ('d.log',fsize=8033020, parent = ddir)
    dfil3 = Node('d.ext', fsize=5626152, parent = ddir)
    kfile = Node('k', fsize=7214296, parent = ddir)
    # print(RenderTree(fsroot))

    # print("Size of d:", dirsize(ddir))
    # print("Size of e:", dirsize(edir))
    print("Size of .:", dirsize(adir))

    return

def dirsize(aNode):
    dirsize = 0
    for kid in aNode.children:
        print(kid.name, kid.fsize)
        if kid.fsize > 0:
            dirsize += kid.fsize
        else:   # it's a directory
            dirsize += dirsize(kid)
    return(dirsize)

def process_a():
    do_test()

def process_b():
    return

def process():
    process_a()
    process_b()

if __name__ == "__main__":
    process()
