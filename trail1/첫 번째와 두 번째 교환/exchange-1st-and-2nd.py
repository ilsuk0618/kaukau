a=input()
arr=[0]*len(a)
b=a[0]
c=a[1]
for i in range(len(a)):
    if a[i]==b and arr[i]!=1:
        arr[i]+=1
        a = a[0:i]+c+a[i+1:]
        

for i in range(len(a)):
    if a[i]==c and arr[i]!=1:
        arr[i]+=1
        a = a[0:i]+b+a[i+1:]

print(a)