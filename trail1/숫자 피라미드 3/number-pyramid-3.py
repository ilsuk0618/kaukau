i=int(input())
cnt=1

for j in range(i):
    cnt=j+1
    for k in range(j+1):
        print(cnt, end=" ")
        cnt+=j+1
    print()