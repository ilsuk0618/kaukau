n = int(input())

def type(n):
    if n==0:
        return
    type(n-1)
    print("HelloWorld")

type(n)