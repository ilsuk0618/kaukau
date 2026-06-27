n = int(input())
arr = list(map(int, input().split()))

def finda(n, arr):
    if n==1:
        return arr[0]

    a=finda(n-1,arr)

    if a>arr[n-1]:
        return a
    else:
        return arr[n-1]

print(finda(n,arr))