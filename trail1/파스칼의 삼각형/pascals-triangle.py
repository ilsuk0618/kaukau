n=int(input())

arr=[[0 for _ in range(n)]
for _ in range(n)]

for i in range(n):
    for j in range(n):
        if j==0:
            arr[i][j]=1
        elif i!=0 and j!=0:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for elem in arr:
    for ans in elem:
        if ans!=0:
            print(ans,end=" ")
        else:
            print(" ", end=" ")
    print()