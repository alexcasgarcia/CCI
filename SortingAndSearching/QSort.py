def partition(array,begin,end):
    pivot=begin
    for i in xrange(begin+1,end+1):
        printState(array,pivot,i)
        if array[i]<=array[begin]:
            pivot+=1
            array[i],array[pivot]=array[pivot],array[i]
    array[begin],array[pivot]=array[pivot],array[begin]
    return pivot

def quicksort(array,begin=0,end=None):
    if end is None:
        end=len(array)-1
    if begin>=end:
        return
    pivot=partition(array,begin,end)
    quicksort(array,begin,pivot-1)
    quicksort(array,pivot+1,end)

def printState(array,pivot,i):
    line1=""
    line2=""
    for index,x in enumerate(array):
        line1+=str(x)+"  "
        space=""
        for y in xrange(len(str(x))-1):
            space+=" "
        if index==i:
            line2+="i"+space+"  "
        elif index==pivot:
            line2+="p"+space+"  "
        else:
            line2+=space+"   "
    line2+="\n"
    print line1
    print line2

x=[5,6,7,8,9,1,2,3,4]
quicksort(x)
