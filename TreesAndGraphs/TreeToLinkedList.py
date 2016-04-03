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

print "LinkedListNode Testing"
a = LinkedListNode(5)
b = LinkedListNode(3)
print "Node a: "+str(a)
print "Node b: "+str(b)
print "Next Node for a: "+str(a.getNextNode())
print "Next Node for b: "+str(b.getNextNode())
print "Set b as next node to a"
a.setNextNode(b)
print "Next Node for a: "+str(a.getNextNode())
print "Next Node for b: "+str(b.getNextNode())
print

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if (self.head == None):
            return ""
        trailingNode=self.head
        node=trailingNode.getNextNode()
        myString=str(trailingNode)
        while (node != None):
            myString=myString+"->"+str(node)
            trailingNode=node
            node=trailingNode.getNextNode()
        return myString

    def appendToTail(self,value):
        newNode=LinkedListNode(value)
        if (self.head == None):
            self.head = newNode
        else:
            node=self.head
            while (node.getNextNode() != None):
                node = node.getNextNode()
            node.setNextNode(newNode)

print "LinkedList Testing"
l = LinkedList()
l.appendToTail(1)
print "LinkedList:"+str(l)
l.appendToTail(2)
print "LinkedList:"+str(l)
l.appendToTail(3)
print "LinkedList:"+str(l)
print

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

    def __str__(self):
        return str(self.values)

print "Queue Testing"
q = Queue([])
print "Empty queue: "+str(q)
q.add(1)
q.add(2)
q.add(3)
print "Populated queue: "+str(q)
a=q.remove()
print "Removed "+str(a)+" from queue: "+str(q)
print "isEmpty? "+str(q.isEmpty())
b=q.remove()
c=q.remove()
print "Removed "+str(b)+" and "+str(c)+" from queue: "+str(q)
print "isEmpty? "+str(q.isEmpty())
print

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.children = []

    def __str__(self):
        return str(self.value)

    def getChildren(self):
        return self.children

    def setChildren(self,children):
        self.children=children

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
                linkedListArray+=[LinkedList()]
            linkedListArray[j].appendToTail(node.getValue())

            i+=1
            if(i==k):
                j+=1
                k=2**i
                i=0

            for x in xrange(len(children)):
                q.add(children[x])

        return linkedListArray

print "TreeNode Testing"
a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(5)
f=TreeNode(6)
g=TreeNode(7)
h=TreeNode(8)
i=TreeNode(9)
j=TreeNode(10)
k=TreeNode(11)
l=TreeNode(12)
m=TreeNode(13)
n=TreeNode(14)
o=TreeNode(15)
a.setChildren([b,c])
b.setChildren([d,e])
c.setChildren([f,g])
d.setChildren([h,i])
e.setChildren([j,k])
f.setChildren([l,m])
g.setChildren([n,o])
x=a.toLinkedListArray()
for i in xrange(len(x)):
    print "Linked List "+str(i)+":"+str(x[i])
