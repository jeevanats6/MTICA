def result(s1,s2):
    return[int(i)+int(j) for i,j in zip(s1,s2)]

inp1=input().split()
inp2=input().split()
print(*result(inp1,inp2))

