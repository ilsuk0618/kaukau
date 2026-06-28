n = int(input())
arr = list(map(int, input().split()))

for i in range(0,n,2):
    if i==0:
        print(arr[0],end=" ")
    else:
        arr_1=arr[:1+i]
        arr_1.sort()
        print(arr_1[i//2], end=" ")
    