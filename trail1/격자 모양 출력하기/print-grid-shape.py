n,m=map(int, input().split())

arr=[[0 for _ in range(n)]
for _ in range(n)]

for i in range(m):
    r,c = tuple(map(int, input().split()))
    arr[r-1][c-1]=r*c

for elem in arr:
    for ans in elem: 
        print(ans, end=" ")
    print()