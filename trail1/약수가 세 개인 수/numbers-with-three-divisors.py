start, end = map(int, input().split())
ans=0
for j in range(start, end+1):
    cnt=0
    for k in range(1,j+1):
        if j%k==0:
            cnt+=1
    if cnt==3:
        ans+=1
print(ans)
