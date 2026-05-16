i=int(input())
cnt=9

for j in range(i):
    for k in range(i):
        if cnt>0:
            print(cnt, end="")
            cnt-=1
        elif cnt==0:
            cnt=9
            print(cnt, end="")
            cnt-=1

    print()