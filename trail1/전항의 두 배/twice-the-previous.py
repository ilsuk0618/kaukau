arr=list(map(int, input().split()))

for i in range(2,10):
    arr.append(0)
    arr[i]=arr[i-1]+2*arr[i-2]

print(*arr)