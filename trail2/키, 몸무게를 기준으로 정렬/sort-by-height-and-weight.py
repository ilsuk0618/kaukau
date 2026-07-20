n = int(input())

class Student:
    def __init__ (self, name, l, w):
        self.name=name
        self.l=l
        self.w=w
students=[]
for _ in range(n):
    name, l, w = tuple(map(str, input().split()))
    students.append(Student(name,l,w))

students.sort(key=lambda x : (int(x.l), -int(x.w)))

for student in students:
    print(student.name, student.l, student.w)