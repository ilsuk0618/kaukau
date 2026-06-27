N = int(input())

def calc(N):
    if N==1:
        return 2
    if N==2:
        return 4

    return calc(N-1)*calc(N-2)%100

print(calc(N))
    