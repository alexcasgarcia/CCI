#methods for mergesort and quicksort


def mergesort(array):
	helper = [None]*len(array)
	print "array = %s" % ((array,))
	print "helper = %s" % ((helper,))
	_mergesort(array, helper, 0, len(array)-1,0)		
	return None


def _mergesort(array, helper, low, high,step): 
	blank = ""
	for x in xrange(step):
		blank += "    "
	print ""
	print "%s _mergesort" % ((blank,))
	print "%s array = %s" % ((blank,array))
	print "%s helper = %s" % ((blank,helper))
	print "%s low = %s" % ((blank,low))
	print "%s high = %s" % ((blank,high))
	if (low < high):
		middle = int((low+high)/2)
		print "%s middle = %s" % ((blank,middle))
		_mergesort(array, helper, low, middle,step+1)
		_mergesort(array, helper, middle+1,high,step+1)
		merge(array, helper, low, middle, high,step)
	return None

def merge(array, helper, low, middle, high,step):
	blank = ""
	for x in xrange(step):
		blank += "    "
	print ""
	print "%s merge" % ((blank,))
	print "%s low = %s" % ((blank,low))
	print "%s high = %s" % ((blank,high))
	for i in xrange(low, high):
		helper[i] = array[i] 
	print "%s helper=%s" % ((blank,helper))

	helperLeft = low
	helperRight = middle+1
	current = low

	print "%s helperLeft = %s" % ((blank,helperLeft))
	print "%s helperRight = %s" % ((blank,helperRight))
	print "%s current = %s" % ((blank,current))

	while (helperLeft <= middle and helperRight <= high):
		if (helper[helperLeft] <= helper[helperRight]):
			array[current] = helper[helperLeft]
			helperLeft+=1
		else:
			array[current] = helper[helperRight]
			helperRight+=1
		current+=1

	remaining=middle-helperLeft
	for i in xrange(remaining+1):
		array[current+1] = helper[helperLeft+1]
	return None

a = [9,1,3,5,2,0,7,6,4,8]
print a
mergesort(a)
print a






