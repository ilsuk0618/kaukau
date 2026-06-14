m=int(input())
cnt=0
for _ in range(m):
    n=int(input())
    cnt+=n
n=str(cnt)
for i in range(1,len(n)):
    print(n[i],end="")
print(n[0])