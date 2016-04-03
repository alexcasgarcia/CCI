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

    def addChild(self,node):
        self.children += [node]

    def getChildren(self):
        return self.children

    def getValue(self):
        return self.value

    def visit(self):
        self.visited = True

    def mark(self):
        self.marked = True

    def unmark(self):
        self.marked = False

    def wasMarked(self):
        return self.marked

    def reset(self):
        if (self == None):
            return
        self.unmark()
        children = self.getChildren()
        for x in xrange(len(children)):
            if (children[x].wasMarked == True):
                children[x].reset()


    def search(self,target):
        q = Queue([])
        q.add(self)
        self.mark()

        while (q.isEmpty() == False):
            node = q.remove()
            if (node.getValue() == target.getValue()):
                return True
            children = node.getChildren()
            for x in xrange(len(children)):
                if (children[x].wasMarked() == False):
                    children[x].mark()
                    q.add(children[x])
        return False

    def findRoute(self, target):
        if (self.search(target)):
            return True
        else:
            self.reset()
            return target.search(self)



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
print "Search"
print n1.findRoute(n10)

e = Node(5,[])
d = Node(4,[e])
c = Node(3,[d])
b = Node(2,[c])
a = Node(1,[b])

print "Search2"
print a.findRoute(e)

e = Node(5,[])
d = Node(4,[e])
c = Node(3,[d])
b = Node(2,[c])
a = Node(1,[b])
print "Search3"
print e.findRoute(a)

