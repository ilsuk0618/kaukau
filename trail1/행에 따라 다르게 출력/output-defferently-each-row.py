i=int(input())
cnt=1
cnt2=i+2

for j in range(i):
    if j%2==0:
        for k in range(i):
            print(cnt, end=" ")
            cnt+=1
        cnt=cnt+2*i
    else:
        for k in range(i):
            print(cnt2, end=" ")
            cnt2+=2
        cnt2=cnt2+i
    print()