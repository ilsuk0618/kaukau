n = int(input())
arr = list(map(int, input().split()))

def find(n, arr):
    for i in range(n):
        if int(arr[i])%2==0:
            arr[i]=str(int(arr[i])//2)

    for elem in arr:
        print(elem, end=" ")

find(n,arr)