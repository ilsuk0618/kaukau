n=int(input())

arr_2d=[[0 for _ in range(n)]
for _ in range(n)
]

if n%2==0:
    num=n**2-n+1
else:
    num=n**2

if n%2==0:
    num2=1
    num3=2*n-1
else:
    num2=2*n-1
    num3=1
num4=num

for i in range(n):
    for j in range(n):
        if n%2!=0:
            if j%2!=0:
                arr_2d[i][j]=num
                num-=num3
            else: 
                arr_2d[i][j]=num
                num-=num2
        else:
            if j%2!=0:
                arr_2d[i][j]=num
                num-=num3
            else: 
                arr_2d[i][j]=num
                num-=num2  
    if n%2==0:
        num4+=1
        num2+=2
        num3-=2
    else:
        num4-=1
        num2-=2
        num3+=2
    num=num4
    

for elem in arr_2d:
    for ans in elem:
        print(ans, end=" ")
    print()
