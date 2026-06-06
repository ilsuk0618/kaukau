n,m=input().split()
cnt=-1
ans=-1

for elem in n:
    cnt+=1
    if elem==m:
        ans=cnt
        break

if ans!=-1:
    print(ans)

elif ans==-1:
    print("No")
