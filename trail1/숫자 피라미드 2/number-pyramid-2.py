i=int(input())
cnt=1

for k in range(i):
    for j in range(k+1):
        print(cnt, end=" ")
        cnt+=1
    print()