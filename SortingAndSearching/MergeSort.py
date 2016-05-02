#merge_sort is a recursive function that takes one argument, the list that you'd like sorted
def merge_sort(m):
    #The base case is if m is empty or a single element.  Then the list is sorted.
    if len(m)<=1:
        return m

    #split the original list up into left and right halves somehow.  Shouldn't really matter how
    left=[]
    right=[]
    for i,x in enumerate(m):
        if i%2==1:
            left.append(x)
        else:
            right.append(x)

    #merge recursively call merge_sort to eventually get to the base case.
    left=merge_sort(left)
    right=merge_sort(right)
    
    return merge(left,right)

def merge(left,right):
    result=[]

    #left and right are guaranteed to be sorted because the output to merge_sort is a sorted list.  While both lists still have elements choose the smaller element to come first.
    while  len(left)>0 and len(right)>0:
        if left[0]<=right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    #once you exhause one of the left or right lists you can just copy the rest of the list into your result, you know that it will be sorted
    while len(left)>0:
        result.append(left.pop(0))
    while len(right)>0:
        result.append(right.pop(0))

    return result
            

x=[10,9,8,7,6,5,4,3,2,1,71,72,73,45,65,43,21]
print "x"
print x
print "merge_sort(x)"
print merge_sort(x)
