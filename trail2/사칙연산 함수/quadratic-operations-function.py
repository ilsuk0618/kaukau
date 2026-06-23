a, o, c = input().split()
a = int(a)
c = int(c)
ans=0

def plus(a,o,c):
    ans=a+c
    return ans
def minus(a,o,c):
    ans=a-c
    return ans
def squa(a,o,c):
    ans=a*c
    return ans
def left(a,o,c):
    ans=a/c
    return int(ans)

if o=="+":
    print(a,o,c,"=",plus(a,o,c))
elif o=="-":
    print(a,o,c,"=",minus(a,o,c))
elif o=="*":
    print(a,o,c,"=",squa(a,o,c))
elif o=="/":
    print(a,o,c,"=",left(a,o,c))
else:
    print("False")