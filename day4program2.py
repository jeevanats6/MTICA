def greet(inpstr):
    outstr="Hello student"+" "+inpstr
    return outstr.title()

inp=input("Enter your name:")
print(greet(inp))
