i=int(input())
cnt=1

for j in range(i):
    cnt=i-j
    for k in range(j+1):
        print(cnt, end=" ")
        cnt+=1
    print()