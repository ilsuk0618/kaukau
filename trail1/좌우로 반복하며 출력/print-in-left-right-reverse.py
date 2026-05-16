i=int(input())
cnt=1

for j in range(i):
    if j%2==0:
        cnt=1
        for h in range(i):
            print(cnt, end="")
            cnt+=1
        
    else:
        cnt=i
        for h in range(i):
            print(cnt, end="")
            cnt-=1
    print()
        
