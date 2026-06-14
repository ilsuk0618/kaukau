m=input()
n=input()
cnt=0
while True:
    if cnt==len(m):
        print("-1")
        break
    elif m==n:
        print(cnt)
        break
    else:
        m=m[len(m)-1]+m[0:len(m)-1]
        cnt+=1
