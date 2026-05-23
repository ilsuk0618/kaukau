start, end = map(int, input().split())
ans=0

for i in range(start, end+1):
    cnt=0
    for j in range(1,i+1):
        if i%j==0 and j!=i:
            cnt+=j
    if cnt==i:
        ans+=1
print(ans)