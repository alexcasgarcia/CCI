def parens(n,op):
    a=[]
    b=[]
    if (n==op or op>0):
        if (n==0):
            return ['']
        else:
            a=parens(n-1,op-1)
            a=[x+'(' for x in a]
    if (n>0 and n!=op):
        b=[x+')' for x in parens(n,op+1)]
    return a+b

print parens(1,0)
print parens(2,0)
print parens(4,0)


def perm(string):
    inner_perm_list=[]
    perm_list=[]
    if len(string)==1:
        return [string]
    for x in string:
        rem_string=''
        for y in string:
            if (y!=x):
                rem_string+=y
        inner_perm_list=perm(rem_string)
        for t in inner_perm_list:
            perm_list.append(x+t)
    return perm_list

print perm('ABCD')
print perm('ABC')
print perm('AB')

def perm2(string):
    used_characters=[]
    inner_perm_list=[]
    perm_list=[]
    if len(string)==1:
        return [string]
    i=0
    for x in string:
        if x not in used_characters:
            used_characters.append(x)
            rem_string=''
            j=0
            for y in string:
                if (i!=j):
                    rem_string+=y
                j+=1
            inner_perm_list=perm2(rem_string)
            for t in inner_perm_list:
                perm_list.append(x+t)
        i+=1
    return perm_list

print perm2('AAB')
print perm2('AABAA')
