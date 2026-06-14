a,b=map(int,input().split())
c=a+b
cnt=0
for elem in str(c):
    if elem=="1":
        cnt+=1
print(cnt)