class LinkedListNode:
    def __init__(self,value):
        self.value=value
        self.nextNode = None 

    def __str__(self):
        return str(self.value)

    def getNextNode(self):
        return self.nextNode
    
    def setNextNode(self,newNode):
        self.nextNode = newNode

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        myString = ""
        if (self.head == None):
            return myString

        trailingNode=self.head
        node=trailingNode
        myString=str(trailingNode)
        while (node.getNextNode() != None):
            myString=myString+"->"+str(trailingNode)
            trailingNode=node
            node=trailingNode.getNextNode()
        return myString

    def appendToTail(self,value):
        print "append: " + str(value)
        newNode=LinkedListNode(value)

        trailingNode = self.head
        node = trailingNode
        if (trailingNode == None):
            self.head=newNode
        else:
            while (node.getNextNode() != None):
                trailingNode = node
                node = trailingNode.getNextNode()
            trailingNode.setNextNode(newNode)

class Queue:
    def __init__(self,values):
        self.values = values

    def remove(self):
        topOfQueue=self.values[0]
        self.values=self.values[1:]
        return topOfQueue

    def isEmpty(self):
        return eval('len(self.values)==0')

    def add(self,value):
        self.values=self.values+[value]

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.children = []

    def getChildren(self):
        return self.children

    def getValue(self):
        return self.value

    def toLinkedListArray(self):
        q = Queue([])
        q.add(self)
        linkedListArray=[]
        i=0
        j=0
        k=2**j

        while(q.isEmpty() == False):
            node = q.remove()
            children=node.getChildren()
            if(i==0):
                linkedListArray[j]=TreeNode(node.getValue())
            else:
                linkedListArray[j].appendToTail(LinkedListNode(node.getValue))

            i+=1
            if(i==k):
                j+=1
                k=2**i
                i=0

            for x in xrange(len(children)):
                q.add(children[x])

l = LinkedList()
l.appendToTail(1)
l.appendToTail(2)
l.appendToTail(3)
l.appendToTail(4)
print str(l)
