class MyStack:
    def __init__(self,values):
        self.values = values

    def __str__(self):
        return str(self.values)

    def __len__(self):
        return len(self.values)

    def pop(self):
        try:
            topOfStack = self.values[0]
            self.values = self.values[1:]
            return topOfStack
        except IndexError:
            return None

    def push(self,value):
        self.values = [value] + self.values

    def peek(self):
        try:
            return self.values[0]
        except IndexError:
            return None

    def isEmpty(self):
        return eval('len(self.values) == 0')

class MyQueue:
    def __init__(self,values):
        self.psuedoQueue = MyStack(values) 

    def __str__(self):
        return str(self.psuedoQueue)

    def __len__(self):
        return len(self.psuedoQueue)

    def isEmpty(self):
        return self.psuedoQueue.isEmpty()

    def peek(self):
        return self.psuedoQueue.peek()

    def remove(self):
        return self.psuedoQueue.pop()

    def add(self,value):
        tempStack = MyStack([])
        for x in xrange(len(self.psuedoQueue)): 
            tempStack.push(self.psuedoQueue.pop())

        tempStack.push(value)

        for x in xrange(len(tempStack)):
            self.psuedoQueue.push(tempStack.pop())


x = [1,2,3,4,5]
q = MyQueue(x)
print "values: " + str(q)
print "isEmpty: " + str(q.isEmpty())
print "peek: " + str(q.peek())
print "remove: " + str(q.remove())
print "values: " + str(q)
print "add: " + str(q.add(8))
print "values: " + str(q)



