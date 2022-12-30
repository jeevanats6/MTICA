def printseries(ch,n):
    sp='_'
    for i in range(0,n):
        print(sp*(n-i-1) +ch*(2*i+1)+sp*(n-i-1))
    return None

inpch=input()        
inpnum=int(input())
printseries(inpch,inpnum)
