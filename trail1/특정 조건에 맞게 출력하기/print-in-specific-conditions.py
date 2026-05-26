arr=list(map(int, input().split()))
arr2=[]
for i in range(len(arr)):
    k=arr[i]
    if k!=0 and k%2==0:
        arr[i] = k//2
        arr2.append(arr[i])
    elif k!=0 and k%2!=0:
        arr[i] = k+3
        arr2.append(arr[i])
    else:
        break
print(*arr2)