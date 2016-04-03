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

    def isBST(self,minVal,maxVal):
        value=self.getValue()
        children=self.getChildren()
        operators=['<','>=']
        bounds=[maxVal,minVal]
        for x in xrange(len(children)):
            child=children[x]
            checkChild=True
            if (bounds[x]!=None and not eval('value'+operators[x]+''+str(bounds[x]))):
                checkChild=False
            print str(x)+"th child "+str(child.getValue())+''+str(operators[x])+''+str(value)
            if(eval('child.getValue()'+str(operators[x])+'value')):
                if (x==0):
                    leftBranchBST=child.isBST(None,value)
                if (x==1 and leftBranchBST):
                    return child.isBST(value,None)
            else:
                return False
        return True


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
print a.isBST(None,None)

a=TreeNode(2)
b=TreeNode(1)
c=TreeNode(3)
a.setChildren([b,c])
b.setChildren([])
c.setChildren([])
print a.isBST(None,None)

a=TreeNode(17)
b=TreeNode(9)
c=TreeNode(25)
d=TreeNode(5)
e=TreeNode(12)
f=TreeNode(18)
g=TreeNode(27)
h=TreeNode(1)
i=TreeNode(7)
j=TreeNode(11)
a.setChildren([b,c])
b.setChildren([d,e])
c.setChildren([f,g])
d.setChildren([h,i])
e.setChildren([j])
print a.isBST(None,None)


