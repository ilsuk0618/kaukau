n = int(input())

def type(a):
    if a==n+1:
        return
    
    print(a, end=" ")
    type(a+1)
        
def type2(n):
    if n==0:
        return

    print(n, end=" ")
    type2(n-1)

type(1)
print()
type2(n)
