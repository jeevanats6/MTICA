spins={('red', '18'),('black', '17'),('orange', '17'),
       ('red', '16'),('black', '15'),('orange', '19'),
       ('red', '4'),('black', '18'),('orange', '14'),
       ('red', '8'),('black', '11'),('orange', '12')}
def countblacks(aList):
    count=0
    for color,number in aList:
        if color =='red':
            yield count
            couunt=0
        else:
            count +=1
    yield count
gaps= [gap for gap in countblacks(spins)]
print(gaps)
            
