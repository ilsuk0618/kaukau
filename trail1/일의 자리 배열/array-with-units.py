arr=list(map(int, input().split()))

for i in range(8):
    arr.append(0)
    arr[i+2]=arr[i]+arr[i+1]
    a=arr[i+2]%10

    arr[i+2]=a

print(*arr)