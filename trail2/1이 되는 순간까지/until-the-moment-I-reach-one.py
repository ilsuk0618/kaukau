N = int(input())

def share(N):
    if N==1:
        return 0

    elif N%2==0:
        return share(N//2) + 1

    else:
        return share(N//3) +1

print(share(N))