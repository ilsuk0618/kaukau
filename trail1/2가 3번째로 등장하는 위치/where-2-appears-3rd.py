cnt=0
cnt2=0
a=int(input())
arr=list(map(int, input().split()))

for elem in arr:
    if cnt<3:
        if elem==2:
            cnt+=1
    elif cnt==3:
        break
    cnt2+=1

print(cnt2)
    