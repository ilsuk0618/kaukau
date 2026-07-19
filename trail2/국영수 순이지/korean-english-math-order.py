n = int(input())

class Students:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math


students = []
for _ in range(n):
    name, kor, eng, math = tuple(map(str, input().split()))
    students.append(Students(name, kor, eng, math))

students.sort(key=lambda x : (-int(x.kor), -int(x.eng), -int(x.math)))

for student in students:
    print(student.name, student.kor, student.eng, student.math)

