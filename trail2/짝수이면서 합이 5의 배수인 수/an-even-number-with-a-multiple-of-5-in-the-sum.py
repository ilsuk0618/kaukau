n = int(input())

def panda_0(n):
    if n%2==0:
        a=n//10
        b=n%10
        if (a+b)%5==0:
            print("Yes")
        else:
            print("No")
    else:
            print("No")
            
panda_0(n)