m,n=map(str,input().split())
cnt=0
for _ in range(int(m)):
    a=input()
    if a==n:
        cnt+=1
print(cnt)