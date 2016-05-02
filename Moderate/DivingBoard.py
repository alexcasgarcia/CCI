#Recursive solution
def allLengths(k,shorter,longer):
    lengths={}
    getAllLengths(k,0,shorter,longer,lengths)
    return lengths.keys()

def getAllLengths(k,total,shorter,longer,lengths):
    if k==0:
        lengths[total]=1
        return
    getAllLengths(k-1,total+shorter,shorter,longer,lengths)
    getAllLengths(k-1,total+longer,shorter,longer,lengths)

#The recursive solution has 2 methods
#allLengths and getAllLengths
#getAllLengths gets called recursively after the initial call within allLengths
#allLengths creates a dictionary which gets modified in place by the getAllLengthsRecursive method and then we return the keys from the lengths dictionary.
#getAllLengths does not return anything
#for the base case, k=0, we we add the total to the lengths dictionary.
#Notice how even though lengths is a dummy variable in the recursive method the outer lengths in the allLengths method retains all the changes made to it by the recursive call.
#The reduce step calls the getAllLengths method with k-1 once with total+shorter and once with total+longer
#Calculating runtime
#every single time getAllLengths is called we call getAllLengths 2 more times.
# This gives us a runtime of O(2^k), very bad

print "Run allLengths"
print allLengths(10,2,3)

#Memoized solution
def allLengthsMemo(k,shorter,longer):
    lengths={}
    visited={}
    getAllLengthsMemo(k,0,shorter,longer,lengths,visited)
    return lengths.keys()

def getAllLengthsMemo(k,total,shorter,longer,lengths,visited):
    if k==0:
        lengths[total]=1
        return
    key=str(k)+" "+str(total)
    if visited.get(key):
        return
    getAllLengthsMemo(k-1,total+shorter,shorter,longer,lengths,visited)
    getAllLengthsMemo(k-1,total+longer,shorter,longer,lengths,visited)
    visited[key]=1

#This is the same algorithm as above but memoized
#visited is the dictionary we use for memoization.
#first pass an empty visited dictionary to the gerAllLengthsMemo

print "Run allLengthsMemo"
print allLengthsMemo(50,2,3)


def allLengthsOptimal(k,shorter,longer):
    if shorter==longer:
        return [k*shorter]
    else:
        output=[]
        for x in xrange(k+1):
            output.append(x*shorter+(k-x)*longer)
        return output

print allLengthsOptimal(50,2,3)
            
