n = int(input())

class Student:
    def __init__ (self, l, w, num):
        self.l=l
        self.w=w
        self.num=num
students=[]
for i in range(n):
    l, w, num = tuple(map(str, input().split()))+(i+ 1,)
    students.append(Student(l,w,num))

students.sort(key=lambda x : (int(x.l), -int(x.w)))

for student in students:
    print(student.l, student.w, student.num)