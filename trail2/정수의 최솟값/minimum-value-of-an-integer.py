a, b, c = map(int, input().split())

def finding_0(a,b,c):
    cnt=100
    arr=[]
    arr.append(a)
    arr.append(b)
    arr.append(c)
    for elem in arr:
        if elem<cnt:
            cnt=elem
    return cnt

ans=finding_0(a,b,c)

print(ans)