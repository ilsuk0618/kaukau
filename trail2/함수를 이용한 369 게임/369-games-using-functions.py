a, b = map(int, input().split())

def chenk_0(i):
    arr=[]
    arr.append(str(i))
    cnt=0
    for elem in arr:
        for j in elem:
            if j=="3" or j=="6" or j=="9":
                cnt+=1
    if cnt==0:
        return 0
    else:
        return 1

def panda_0(a,b):
    cnt=0
    for i in range(a,b+1):
        if i%3==0 or chenk_0(i):
            cnt+=1
    print(cnt)
panda_0(a,b)