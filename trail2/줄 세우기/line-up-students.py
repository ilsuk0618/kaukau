class Student:
    def __init__(self, leng, poun, num):
        self.leng=leng
        self.poun=poun
        self.num=num

students=[]
n=int(input())

for i in range(n):
    leng, poun, num = tuple(map(int, input().split()))+(i+1,)
    students.append(Student(leng, poun, num))

students.sort(key=lambda x : (-x.leng, -x.poun, x.num))

for student in students:
    print(student.leng, student.poun, student.num)