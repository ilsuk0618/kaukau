i=int(input())
arr=list(map(int,input().split()))
arr2=[]
for k in range(i):
    if arr[k]%2==0:
        arr2.append(arr[k])
print(*arr2)