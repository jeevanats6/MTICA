def extract_SpecialCharacter(s):
    n_SpecialCharacter=0
    for i in s:
        if i in '123456987':
            n_SpecialCharacter+=1
    return n_SpecialCharacter

str1=input()
a=extract_SpecialCharacter(str1)
print(" No of Digits in:'",str1,"'is",a)

