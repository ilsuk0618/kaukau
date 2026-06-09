m,n = input().split()
cnt=0
for elem in m:
    if 46<ord(elem)<58:
        cnt+=1
        a=m[:cnt]
    else:
        break
cnt=0

for elem in n:
    if 46<ord(elem)<58:
        cnt+=1
        b=n[:cnt]
    else:
        break
print(int(a)+int(b))