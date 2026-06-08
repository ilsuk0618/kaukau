a=input()
b=len(a)
a=a[0:1]+a[2:b-2]+a[b-1:b]
print(a)