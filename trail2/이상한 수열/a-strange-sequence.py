N = int(input())

def calc(N):
    if N==1:
        return 1
    if N==2:
        return 2

    return calc(N//3)+calc(N-1)

print(calc(N))