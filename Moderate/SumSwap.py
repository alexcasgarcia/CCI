def findPair(arr1,arr2):
    sum1=sum(arr1)
    sum2=sum(arr2)
    arr1.sort()
    arr2.sort()
    for x in arr1:
        want1=x+(sum1-sum2)/2
        want2=x+(sum2-sum1)/2
        for y in arr2:
            if y==want1:
                return [x,y]
            elif y==want2:
                return [x,y]
            elif y>want1 and y>want2:
                break

def bruteForce(arr1,arr2):
    sum1=sum(arr1)
    sum2=sum(arr2)
    for x in arr1:
        for y in arr2:
            if sum1-x+y==sum2+x-y:
                return [x,y]
    return 0

def optimalPair(arr1,arr2):
    hash1={}
    for 
arr1=[4,1,2,1,1,2]
arr2=[3,6,3,3]
print findPair(arr1,arr2)
