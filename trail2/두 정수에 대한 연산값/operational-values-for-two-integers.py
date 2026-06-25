a, b = map(int, input().split())

def fin(a,b):
    if a>b:
        a=a+25
        b=b*2
    else:
        b=b+25
        a=a*2
    return a,b

a, b = fin(a,b)
print(a,b)