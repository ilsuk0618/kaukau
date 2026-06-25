n = int(input())
arr = list(map(int, input().split()))

def plus(n, arr):
    for i in range(n):
        if int(arr[i])<0:
            arr[i]= int(arr[i])*(-1)

    return arr

arr=plus(n,arr)
for elem in arr:
    print(elem, end=" ")