arr=list(map(int, input().split()))
ans=0
ans2=0
for i in range(1,10,2):
    ans+=arr[i]
for i in range(2,10,3):
    ans2+=arr[i]
ans2=ans2/3

print(f"{ans} {ans2:.1f}")