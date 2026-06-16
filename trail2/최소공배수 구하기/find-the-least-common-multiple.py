n, m = map(int, input().split())

def finding_a(n,m):
    cnt=0
    while True:
        cnt+=1
        if cnt%n==0 and cnt%m==0:
            print(cnt)
            break
        

finding_a(n,m)