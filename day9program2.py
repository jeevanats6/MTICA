def printSeries(n):
    num=1
    for i in range(1,n+1):
        for j in range(i):
            print(num,end='')
            num+=1
##    assert isinstance(ch,str),"First argument should be string"
##    assert isinstance(n,str),'Second argument should be int'
##    for i in range(n,0,-1):
##        print(ch*i)
    return None

inpch=int(input())
##inpNum=int(input("Enter a no:"))
##
##print('-'*40)
##try:
##except AssertionError as ob:
##    print(ob)
##


