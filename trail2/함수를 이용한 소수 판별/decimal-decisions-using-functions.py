a, b = map(int, input().split())

def finda_0(a,b):
    ans=0
    for i in range(a,b+1):
        cnt=0
        for j in range(2,101):
            if i%j==0:
                cnt+=1
        if cnt==1:
            ans+=i
    print(ans)
    
finda_0(a,b)