import math

class Heap:
	def __init__(self,values):
		self.values = values
		self.build_max_heap()
	    
	def __str__(self):
		return str(self.values)

	def size(self):
		return len(self.values)

	def leftChild(self,node):
		return 2*node

	def rightChild(self,node):
		return 2*node+1

	def max_heapify(self,node):
		left = self.leftChild(node)
		right = self.rightChild(node)

		if (left <= self.size() and self.values[left-1] > self.values[node-1]): 
			largestNode = left
		else:
			largestNode = node

		if (right<= self.size() and self.values[right-1] > self.values[largestNode-1]): 
			largestNode = right

		if (largestNode != node):
			self.values[node-1],self.values[largestNode-1] = self.values[largestNode-1],self.values[node-1]
			self.max_heapify(largestNode)


	def build_max_heap(self):
		node=int(len(self.values)/2)
		print "Node: %s" % ((node,))
		while (node > 0):
			self.max_heapify(node)
			node -= 1

def copyToPrintTuple(self,printList,spaceNumber):
	for x in xrange(spaceNumber):
		spaceStr += " "

	for x in printList:
		printTuple += (spaceStr,x)

	return printTuple

def draw(self):
	levels = int(math.log(self.size(),2))

	for x in xrange(levels+1):
		printStr = " "
		for y in xrange(2**x):
			printStr += "%s%s"
		print printStr % (self.copyToPrintTuple(self.values[2**(levels-1)) 






myList=[1,2,3,4,5,6,11,21,12,15,19,20,4,5,7,2,20]
#myList=[1,2,3]
print myList
myHeap = Heap(myList)
print myHeap
