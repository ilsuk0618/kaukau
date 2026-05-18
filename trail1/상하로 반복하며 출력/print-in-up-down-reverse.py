i=int(input())
cnt=1
cnt1=i
for k in range(i):
    for j in range(i):
        if j%2==0:
            print(cnt,end="")
        
        else:
            print(cnt1,end="")
    print()
    cnt+=1
    cnt1-=1
