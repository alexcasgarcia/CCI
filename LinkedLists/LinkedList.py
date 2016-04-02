import sys
class Node:
    def __init__(self,value):
        self.value = value
        self.nextNode = None

    def __str__(self):
        return str(self.value)

    def getValue(self):
        return self.value

    def printLinkedList(self):
        sys.stdout.write(str(self))
        nextNode = self.nextNode
        if (nextNode != None):
            sys.stdout.write('->')
        while (nextNode != None):
            sys.stdout.write(str(nextNode))
            nextNode = nextNode.getNextNode()
            if (nextNode != None):
                sys.stdout.write('->')
        print

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self,node):
        self.nextNode = node

    def appendToTail(self,node):
        thisNode = self
        nextNode = thisNode.nextNode
        while (nextNode != None):
            thisNode = nextNode
            nextNode = thisNode.getNextNode()

        thisNode.setNextNode(node)

