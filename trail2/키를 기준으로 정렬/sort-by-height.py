n = int(input())

class Students:
    def __init__(self,name,leng,pou):
        self.name = name
        self.leng = leng
        self.pou = pou


students = []
for _ in range(n):
    name, leng, pou = tuple(map(str, input().split()))
    students.append(Students(name,leng,pou))

students.sort(key=lambda x : int(x.leng))

for student in students:
    print(student.name, student.leng, student.pou)

