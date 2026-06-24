a, b = map(int, input().split())

def find1(i):
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        return find2(i)
    else:
        return False

def find2(i):
    ans=0
    arr=[]
    arr.append(str(i))
    for elem in arr:
        for k in elem:
            ans+=int(k)
    if ans%2==0:
        return True
    else:
        return False
goal=0
for i in range(a,b+1):
    if find1(i):
        goal+=1
print(goal)