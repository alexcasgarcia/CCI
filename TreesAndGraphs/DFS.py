class Queue:
    def __init__(self,values):
        self.values = values 

    def __str__(self):
        return str(self.values)

    def add(self,value):
        self.values = self.values + [value]

    def remove(self):
        beginningOfQueue = self.values[0]
        self.values = self.values[1:]
        return beginningOfQueue

    def peek(self):
        return self.values[0]

    def isEmpty(self):
        return eval('len(self.values) == 0')

class Node:
    def __init__(self,value,children):
        self.value = value
        self.children = children
        self.visited = False
        self.marked = False

    def __str__(self):
        return str(self.value)

    def addChild(self,value):
        self.children += Node(value,[])

    def getChildren(self):
        return self.children

    def visit(self):
        print str(self)
        self.visited = True

    def mark(self):
        self.marked = True

    def wasVisited(self):
        return self.visited

    def depthfirstsearch(self):
        if (self == None):
            return
        self.visit()
        children = self.getChildren()
        for x in xrange(len(children)):
            if (children[x].wasVisited() == False):
                children[x].depthfirstsearch()

    def breadthfirstsearch(self):
        q = Queue([])
        self.mark()
        q.add(self)

        while (q.isEmpty() == False):
            node = q.remove()
            node.visit()
            children = node.getChildren()
            for x in xrange(len(children)):
                if (children[x].wasVisited() == False):
                    children[x].mark()
                    q.add(children[x])




n4 = Node(4,[])
n5 = Node(5,[])
n6 = Node(6,[])
n7 = Node(7,[])
n8 = Node(8,[])
n9 = Node(9,[])
n10 = Node(10,[])
n2 = Node(2,[n4,n5,n6])
n3 = Node(3,[n7,n8,n9,n10])
n1 = Node(1,[n2,n3])
print "Breadth First Search"
n1.breadthfirstsearch()

n4 = Node(4,[])
n5 = Node(5,[])
n6 = Node(6,[])
n7 = Node(7,[])
n8 = Node(8,[])
n9 = Node(9,[])
n10 = Node(10,[])
n2 = Node(2,[n4,n5,n6])
n3 = Node(3,[n7,n8,n9,n10])
n1 = Node(1,[n2,n3])
print "Depth First Search"
n1.depthfirstsearch()

