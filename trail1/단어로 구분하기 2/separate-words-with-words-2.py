arr=[input().split()]
cnt=0
for elem in arr:
    for ans in elem:
        if cnt%2==0:
            print(ans)
            cnt+=1
        else:
            cnt+=1
            