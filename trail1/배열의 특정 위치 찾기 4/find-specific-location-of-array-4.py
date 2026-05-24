arr=map(int, input().split())
cnt=0
ans=0

for elem in arr:
    if elem!=0 and elem%2==0:
        cnt+=1
        ans+=elem
    elif elem==0:
        break
print(cnt, ans)