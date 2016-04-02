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

    def detectLoop(self):
        nodeArray = []
        node1 = self
        node2 = node1.getNextNode()
        while (node2 != None):
            nodeArray += [node1]
            for x in xrange(len(nodeArray)):
                print "compare " + str(node2) + " and " + str(nodeArray[x])
                if (node2.getValue() == nodeArray[x].getValue()):
                    return node2.getValue()
            node1 = node2
            node2 = node1.getNextNode()
        return None 




head = Node(1)
head.printLinkedList()
head.setNextNode(Node(2))
mid = Node(10)
head.appendToTail(Node(mid))
head.appendToTail(Node(4))
head.appendToTail(Node(5))
head.appendToTail(Node(mid))
head.printLinkedList()
print str(head.detectLoop())


