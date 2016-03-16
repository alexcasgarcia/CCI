import math

class Heap:
    def __init__(self,values):
        self.values = values
        self.build_max_heap()
    
    def __str__(self):
        return str(self.values)

    def max_heapify(self,node):
        if self.values[2*node-1] >= self.values[2*node]:
            maxChildNode = 2*node-1
        else:
            maxChildNode = 2*node

        if self.values[node] < self.values[maxChildNode]:
            self.values[node],self.values[maxChildNode] = self.values[maxChildNode],self.values[node]

    def build_max_heap(self):
        node=int(len(self.values)/2)
        while (node > 0):
            print node
            self.max_heapify(node)
            node -= 1

myList=[1,2,3,4,5,6,11,21,12,15,19,20,4,5,7,2,20]
print myList
myHeap = Heap(myList)
print myHeap
