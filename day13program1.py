def demo_yield():
    print("code segment1 execute1")
    x=7
    yield x*x
    print("code segment2 executed")
    yield 2
    print("code segment3 executed")
    yield 3
    print("code segment4 executed")
        
    
