a=input()
b=a[0]
c=a[1]

for i in range(len(a)):
    if a[i]==c:
        a=a[0:i]+b+a[i+1:]

print(a)