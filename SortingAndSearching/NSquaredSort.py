# Start at the beginning of the array and swap the first two elements if the first is greater than the second.  Then go to the next pair, and so one, continuously making sweeps of the array until it is sorted.  In doing so the smaller items slowly "bubble" up the the beginning of the list

def CreateUnsortedList(length):
	myList = [] 
	for x in xrange(length):
		myList += [length - x]	

	return myList

def BubbleSort(list):
	print "Bubble Sort"
	NumberOfSwitches = 0
	NumberOfComparisons = 0
	for i in xrange(len(list)-1):
		IsSorted = True
		for x in xrange(len(list)-1):
			NumberOfComparisons += 1
			if list[x] > list[x+1]:
				NumberOfSwitches += 1
				IsSorted = False
				print "switch %s and %s"% ((list[x],list[x+1]))
				list[x],list[x+1] = list[x+1],list[x]
		if IsSorted:
			break		
	print "Number of switches/comparisons = %s/%s" % (NumberOfSwitches,NumberOfComparisons)
	return list

def SelectionSort(list):
	print "Selection Sort"
        print list
	NumberOfSwitches = 0
	NumberOfComparisons = 0
	for i in xrange(len(list)):
                minElementIndex = i
		for x in xrange(i+1,len(list)):
                    NumberOfComparisons += 1
                    if list[minElementIndex] > list[x]:
                        minElementIndex = x
                NumberOfSwitches += 1
                print "switch %s and %s" % ((list[i],list[minElementIndex]))
                list[minElementIndex],list[i] = list[i],list[minElementIndex]
        return list
                    
unsortedList = CreateUnsortedList(10)
print unsortedList
print BubbleSort(unsortedList)
print BubbleSort([1,2,3,4,9,5,6,7,8,10])
print SelectionSort([12,13,1,5,12,16,29,1,2,3,4,8,9])
