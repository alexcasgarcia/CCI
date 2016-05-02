def partition(array, begin, end):
    pivot = begin
    for i in xrange(begin+1, end+1):
        print array
        if array[i] <= array[begin]:
            pivot += 1
            print "  switch "+str(i)+" and "+str(pivot)
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot-1)
    quicksort(array, pivot+1, end)

partitionTestLists=[
    [1,2,3,4,5,6,7,8,9,10],
    [10,9,1,2,3,4,5,6],
    [6,7,8,9,1,2,3,4,5,6]
]
for testList in partitionTestLists:
    print testList
    print partition(testList,0,len(testList)-1)
    print testList
    print
 
