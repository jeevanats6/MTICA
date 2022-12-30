def printseriesIncreasing(ch,n):
    assert isinstance(ch,str),"first argument should be string"
    assert isinstance(n,int),"second argument should be string"
    for i in range(1,n+1,1):
        print(ch*i)
    return None
def printseriesdecreasing(ch,n):
    for i in range(n,0,-1):
        print(ch*i)
    return None

inpch=input("enter the charectr:")
inpnum=int(input("enter a no:"))
try:    
    printseriesIncreasing(inpch,inpnum)
except AssertionError as ob:
    print(ob)
print('-'*48)

printseriesdecreasing(inpch,inpnum)

