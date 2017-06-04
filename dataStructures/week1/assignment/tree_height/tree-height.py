# python3
#
'''
Ex:
6
1 -1 0 0 1 2

Node 0 is a child of Node 1
Node 1 is the root
Node 2 is a child of Node 0
Node 3 is a child of Node 0
Node 4 is a child of Node 1
Node 5 is a child of Node 2

                1
               / \
              0   4
              | \
              2  3
              |
              5

'''

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self):
        self.children = []
        self.parents = []
    def addChild(self, node):
        self.children.append(node)
    def addParent(self, node):
        self.parents.append(node)

class TreeHeight:
    def read(self):
        #self.n = int(sys.stdin.readline())
        #self.parent = list(map(int, sys.stdin.readline().split()))
        self.n = 5
        self.parent = list(map(int, [4,-1,4,1,1]))

    def compute_height(self):
        nodes = []
        root = -1
        maxHeight = 1

        # Create the nodes based on the size of the tree
        for node in range(self.n):
            nodes.append(Node())
        for childIndex in range(self.n):
            parentIndex = self.parent[childIndex]
            if parentIndex == -1:
                root = childIndex
            else:
                nodes[parentIndex].addChild(nodes[childIndex])
                nodes[childIndex].addParent(nodes[parentIndex])

        for nodeIndex in range(self.n):
            height = 1
            parents = nodes[nodeIndex].parents
            while len(parents) > 0:
                height+=1
                parents = parents[0].parents
                maxHeight = max(height, maxHeight)
        return maxHeight

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
