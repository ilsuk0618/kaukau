m,n=input().split()
a=ord(m)
b=ord(n)
c=a-b
if a-b<0:
    c=b-a
print(a+b, c)