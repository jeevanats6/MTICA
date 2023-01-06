def findFactor(n):
    temp=[]
    for i in range(1,n+1):
        if n%i==0:
            temp.append(i)
    return temp


def findGCD(n1,n2):
    lstn1=findFactor(n1)
    lstn2=findFactor(n2)
    temp=set(lasn1) set(latn2)
            



##a = int(input())
##print(*findFactor(a))
