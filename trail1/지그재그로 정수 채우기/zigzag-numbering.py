n, m = map(int, input().split())

arr_2d=[[0 for _ in range(m)]
for _ in range(n)
]

num=0
num2=2*n-1
num3=1
num4=0

for i in range(n):
    for j in range(m):
        if j%2==0:
            arr_2d[i][j]=num
            num+=num2
        else: 
            arr_2d[i][j]=num
            num+=num3    
    num4+=1
    num=num4
    num2-=2
    num3+=2

for elem in arr_2d:
    for ans in elem:
        print(ans, end=" ")
    print()