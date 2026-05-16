i=int(input())
cnt=1

for j in range(i):
    for k in range(i):
        if cnt<10:
            print(cnt, end="")
            cnt+=1
        else:
            cnt=1
            print(cnt, end="")
            cnt+=1

    print()