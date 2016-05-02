def merge_sort(m):
    if len(m)<=1:
        return m
    
    left=[]
    right=[]
    for i,x in enumerate(m):
        if i%2==0:
            left.append(x)
        else:
            right.append(x)

    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left,right)

def merge(left,right):
    result=[]
    while len(left)>0 and len(right)>0:
        if left[0]<=right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while len(left)>0:
        result.append(left.pop(0))
    while len(right)>0:    
        result.append(right.pop(0))
    return result

x=[9,8,7,6,5,4,3,2,1]
print x
x=merge_sort(x)
print x
