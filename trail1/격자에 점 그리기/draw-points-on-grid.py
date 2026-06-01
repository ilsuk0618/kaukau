n, m = map(int, input().split())

arr1=[[0 for _ in range(n)]
for _ in range(n)]
cnt=1
for i in range(m):
    r,c=tuple(map(int, input().split()))
    arr1[r-1][c-1]=cnt
    cnt+=1

for elem in arr1:
    for ans in elem:
        print(ans, end=" ")
    print()