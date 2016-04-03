def p(string):
    length=len(string)
    if (length<=1):
        return string 
    else:
        for x in xrange(length):
            print string+":"+str(x)
            print "  "+ string[x:x+1]+" p("+string[0:x]+","+string[x+1:]+")"
            string[x:x+1]+p(string[0:x]+string[x+1:])

string='ABCDE'
print p(string)
