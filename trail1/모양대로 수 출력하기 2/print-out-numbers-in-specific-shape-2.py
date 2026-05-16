i=int(input())
cnt=2

for j in range(i):
    for k in range(i):
        if cnt<9:
            print(cnt, end=" ")
            cnt = cnt+2

        else:
            cnt=2
            print(cnt, end=" ")
            cnt = cnt+2

    print()
