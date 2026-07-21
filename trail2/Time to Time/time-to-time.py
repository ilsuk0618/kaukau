a, b, c, d = map(int, input().split())
ans=0

while True:
    if a==c and b==d:
        break

    elif b<60:
        b+=1
        ans+=1
    elif b==60:
        a+=1
        b=0

print(ans)      