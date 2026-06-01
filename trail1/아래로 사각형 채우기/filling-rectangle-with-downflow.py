n=int(input())
arr_2d=[[0 for _ in range(n)]
for _ in range(n) 
]

num=1
num2=1

for i in range(n):
    num=num2
    for j in range(n):
        arr_2d[i][j] = num
        num+=n
    num2 += 1

for elem in arr_2d:
    for ans in elem:
        print(ans, end=" ") 
    print()