def extract_Consonant(s):
    n_Consonant=''
    for i in s:
        if i in 'bcdhmn':
            n_Consonant+=i
    return n_Consonant

str1=input()
a=extract_Consonant(str1)
print("Consonant in:'",str1,"'is",a)

