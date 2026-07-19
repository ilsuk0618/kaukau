n = 5

class Student:
    def __init__(self, name, height, weight):
        self.name=name
        self.height=height
        self.weight=weight

students=[]

for _ in range(n):
    name, height, weight = input().split()
    students.append(Student(name,height,weight))

students.sort(key=lambda x: x.name)
print("name")
for student in students:
    print(student.name, student.height, student.weight)

print()

students.sort(key=lambda x: -int(x.height))
print("height")
for student in students:
    print(student.name, student.height, student.weight)