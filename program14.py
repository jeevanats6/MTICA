def extract_Digit(s):
    n_Digit=0
    for i in s:
        if i in '123456987':
            n_Digit+=1
    return n_Digit

str1=input()
a=extract_Digit(str1)
print(" No of Digits in:'",str1,"'is",a)

