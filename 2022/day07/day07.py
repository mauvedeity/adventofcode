#!env python3 

from anytree import NodeMixin, RenderTree
class FSBase(object):
    foo = 4

class FSObject(FSBase, NodeMixin):
    def __init__(self, fsname, fbytes, parent = None, children = None):
        super(FSObject, self).__init__()
        self.fsname = fsname
        self.fbytes = fbytes
        self.parent = parent
        if children:
            self.children = children



def process_a():
    return

def process_b():
    return

def process():
    process_a()
    process_b()

if __name__ == "__main__":
    process()
