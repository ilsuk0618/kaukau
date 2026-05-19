i=int(input())
cnt=1

for k in range(i):
    for j in range(k):
        print(" ", end=" ")
    for h in range(i-k,0,-1):
        if cnt==10:
            cnt=1
            print(cnt, end=" ")
            cnt+=1
        else:
            print(cnt, end=" ")
            cnt+=1
    print()