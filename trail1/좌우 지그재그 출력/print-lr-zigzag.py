i=int(input())
cnt=1


for j in range(i):
    cnt2=2*i
    if j%2==0:
        for k in range(i):
            print(cnt, end=" ")
            cnt+=1
        cnt+=i

    else:
        cnt2=i*(j+1)
        for k in range(i):
            print(cnt2, end=" ")
            cnt2-=1
        
    print()