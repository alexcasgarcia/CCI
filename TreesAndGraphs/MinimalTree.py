import math
class Queue:
    def __init__(self,values):
        self.values=values

    def add(self,value):
        self.values = self.values + [value]

    def remove(self):
        topOfQueue=self.values[0]
        self.values = self.values[1:]
        return topOfQueue

    def peek(self):
        return self.values[0]

    def isEmpty(self):
        return eval('len(self.values)==0')

class Node:
    def __init__(self,value,leftChild,rightChild):
        self.value=value
        self.marked=False
        self.leftChild=leftChild
        self.rightChild=rightChild
    def __str__(self):
        return str(self.value)
    def mark(self):
        self.marked=True
    def unmark(self):
        self.marked=False
    def isMarked(self):
        return self.marked
    def getLeftChild(self):
        return self.leftChild
    def getRightChild(self):
        return self.rightChild
    def setLeftChild(self,node):
        self.leftChild=node
    def setRightChild(self,node):
        self.rightChild=node
    def printTree(self):
        print self.value
        if (self.leftChild != None):
            self.leftChild.printTree()
        if (self.rightChild != None):
            self.rightChild.printTree()
    def traverse(self):
        q = Queue([])
        self.mark()
        q.add(self)

        while (q.isEmpty() == False):
            node = q.remove()
            print str(node)
            children = [node.getLeftChild(),node.getRightChild()]
            for x in [0,1]:
                if (children[x] != None and children[x].isMarked() == False):
                    children[x].mark()
                    q.add(children[x])

def MinimalTree(sortedArray,start,end):
    if (end < start):
        return None
    middle = int(math.floor((start+end+1)/2))
    n = Node(sortedArray[middle],None,None)
    n.setLeftChild(MinimalTree(sortedArray,start,middle-1))
    n.setRightChild(MinimalTree(sortedArray,middle+1,end))
    return n


n=MinimalTree([1,2,3,4,5,6,7],0,6)
n.traverse()

print 
sortedArray=[6,7,8,9,10,15,16,17,18,19,20,27,34,45,60]
m=MinimalTree(sortedArray,0,len(sortedArray)-1)
m.traverse()
