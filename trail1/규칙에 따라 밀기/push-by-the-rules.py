a=input()
n=input()
b=len(a)
for i in range(len(n)):
    if n[i]=="L":
        a=a[1:]+a[0:1]
    elif n[i]=="R":
        a=a[b-1]+a[0:b-1]

print(a)