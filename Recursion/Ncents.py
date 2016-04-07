def ncents(n):
    if n==0:
        return [[0,0,0,0]]
    coins=[]
    pennies=[[]]
    nickels=[[]]
    dimes=[[]]
    quarters=[[]]
    if n>=1:
        pennies=ncents(n-1)
        for p in pennies:
            p[0]+=1
        coins+=pennies

    if n>=5 and n%5==0:
        nickels=ncents(n-5)
        for ni in nickels:
            ni[1]+=1
        coins+=nickels

    if n>=10 and n%10==0:
        dimes=ncents(n-10)
        for d in dimes:
            d[2]+=1
        coins+=dimes

    if n>=25 and n%25==0:
        quarters=ncents(n-25)
        for q in quarters:
            q[3]+=1
        coins+=quarters
    return coins

print ncents(8)
print ncents(18)
