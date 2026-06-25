N = int(input())

def wor(N):
    if N==0:
        return
    print(N, end=" ")
    wor(N-1)
    print(N, end=" ")

wor(N)