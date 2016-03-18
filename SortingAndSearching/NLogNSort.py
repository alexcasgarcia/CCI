#methods for mergesort and quicksort


def mergesort(array):
	helper = []
	return _mergesort(array, helper, 0, len(array)-1)		


def _mergesort(array, helper, low, high): 
	if (low < high):
		middle = int((low+high)/2)
		left = _mergesort(array, helper, low, middle)
		right = _mergesort(array, helper, middle+1,high)
		return merge(array, helper, low, middle, high)

def merge(array, helper, low, middle, high):
	for i in xrange(low, high+1):
		helper[i] = array[i] #list assignment index out of range?

	helperLeft = low
	helperRight = middle+1
	current = low

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
		array[current+1] = helper[helperLeft+1

	return array





