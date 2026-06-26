N = int(input())

def plus(N):
    if N==1:
        return 1
    if N==2:
        return 2

    return plus(N-2) + N

print(plus(N))