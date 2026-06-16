n, m = map(int, input().split())
cnt=1
def finding_a(n,m):
    for i in range(1,101,1):
        if n%i==0 and m%i==0:
            cnt=i
            
    print(cnt)
finding_a(n,m)