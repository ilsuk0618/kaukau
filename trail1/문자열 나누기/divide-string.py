n=int(input())
arr=list(map(str, input().split()))
cnt=0

for elem in arr:
    for i in elem:
        if cnt==4:
            print(i)
            cnt=0
        else:
            print(i, end="")
            cnt+=1