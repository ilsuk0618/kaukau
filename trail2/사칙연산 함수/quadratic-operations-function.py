a, o, c = input().split()
a = int(a)
c = int(c)

def clac(a,o,c):
    ans=0
    if o=="+":
        ans=a+c
        print(a,o,c,"=",ans)
    elif o=="*":
        ans=a*c
        print(a,o,c,"=",ans)
    elif o=="-":
        ans=a-c
        print(a,o,c,"=",ans)
    elif o=="/":
        ans=a/c
        print(a,o,c,"=",int(ans))
    else:
        print("False") 
clac(a,o,c)