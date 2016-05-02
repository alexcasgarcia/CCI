def quicksort(A,lo,hi):
    if lo<hi:
        p=partition(A,lo,hi)
        quicksort(A,lo,p-1)
        quicksort(A,p+1,hi)
    else:
        return

def partition(A,lo,hi):
    pivot=A[hi]
    done = 0
    bottom=lo-1
    top=hi
    while not done:
        while not done:
            bottom+=1
            if bottom==top:
                done=1
                break
            if A[bottom]>pivot:
                A[top]=A[bottom]
                break

        while not done:
            top=top-1
            if top==bottom:
                done=1
                break
            if A[top]<pivot:
                A[bottom]=A[top]
                break
    A[top]=pivot
    return top
    

x=[10,9,8,7,6,5,4,3,2,1]
print x
quicksort(x,0,9)
print x
