def printseriesIncreasing(ch,n):
    for i in range(1,n+1,1):
        print(ch*i)
    return None
def printseriesdecreasing(ch,n):
    for i in range(n,0,-1):
        print(ch*i)
    return None

inpch=input("enter the charectr:")
inpnum=int(input("enter a no:"))
printseriesIncreasing(inpch,inpnum)
print('-'*48)
printseriesdecreasing(inpch,inpnum)

