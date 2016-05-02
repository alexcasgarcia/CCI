def mergesort(myList):
    if len(myList)>1:
        midpoint=int(len(myList)/2))
        leftSide=mergesort(myList[0:midpoint])
        rightSide=mergesort(myList[midpoint:])
        return merge(leftSide,RightSide)
    else
        return myList

def merge(leftSide,rightSide):
    iLeft=0
    iRight=0
    if leftSide[iLeft]<rightSide[iRight]:
        mergedList.append(leftSide[iLeft])
        iLeft+=1
    else:
        mergedList.append(Side[iLeft])
        iLeft+=1
