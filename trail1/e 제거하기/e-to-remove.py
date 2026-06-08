a=input()

for i in range(len(a)):
    if i!=(len(a)-1):
        if a[i]=="e":
            a = a[0:i]+a[i+1:]
            break
    else:
        a =  a[0:i-2]

print(a)