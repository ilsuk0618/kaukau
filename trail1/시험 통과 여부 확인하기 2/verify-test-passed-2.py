num=int(input())
cnt=0
for _ in range(num):
    arr=map(int, input().split())
    ans=0
    avg=0
    for elem in arr:
        ans+=elem
    avg=ans/4
    if avg>=60:
        print("pass")
        cnt+=1

    else:
        print("fail")
print(cnt)