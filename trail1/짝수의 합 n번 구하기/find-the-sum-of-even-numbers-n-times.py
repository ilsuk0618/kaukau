i=int(input())
for _ in range(i):
    a, b = map(int,input().split())
    cnt=0
    for k in range(a,b+1):
        if k%2==0:
            cnt+=k
    print(cnt)