N = int(input())

def plus(N):
    if N//10==0:
        return (N%10)*(N%10)
    return plus(N//10)+(N%10)*(N%10)

print(plus(N))