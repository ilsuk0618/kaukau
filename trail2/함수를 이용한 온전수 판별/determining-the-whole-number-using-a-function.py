a, b = map(int, input().split())
cnt=0

def find1(i):
    if i %2!=0:
        return find2(i)
        ## return을 첫번째 함수 부터 넣어줘야한다. 단순히 세번째 함수로 간다고 세번째에서 원래로 리턴시키는건 아니다.
    else:
        return False

def find2(i):
    if i%10!=5:
        return find3(i)
    else:
        return False

def find3(i):
    if i%3!=0 or i%9==0:
        return True
    else:
        return False

for i in range(a,b+1):
    if find1(i):
        cnt+=1

print(cnt)
