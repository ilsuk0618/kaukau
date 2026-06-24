n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def fid(a,b,n1,n2):
    i=0
    cnt=0
    if n1!=1:
        for _ in range(n1-1):
            if a[i:i+n2] == b[0:]:
                print("Yes")
                cnt+=1
                break
            i+=1
        if cnt==0:
            print("No")
    elif n1==1:
        print("Yes")
fid(a,b,n1,n2)