a,b = map(int,input().split())

arr=[[0 for _ in range(b)]
for _ in range(a)]

l=1

for i in range(a):
    for k in range(b):
        arr[i][k]=l
        l+=1
        print(arr[i][k], end=" ")
    print()