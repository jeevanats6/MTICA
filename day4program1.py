student=[[22,'joshna',80,82],[58,'sunil',78,83],
         [49,'sabiha',72,80],[35,'manohar',85,86]]
student.sort()
print(student)
student.sort(key=lambda temp:temp[2])
print(student)
student.sort(key=lambda temp:temp[3])
print(student)
