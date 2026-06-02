n=int(input())
arr=[input()
for _ in range(n)]
i=input()
cnt=0
ans=0

for elem in arr:
    if elem[0]==i:
        cnt+=1
        ans+=len(elem)
print(cnt, f"{ans/cnt:.2f}")