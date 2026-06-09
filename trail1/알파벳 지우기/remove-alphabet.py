m=input()
n=input()
m1=""
n1=""
for i in m:
    if 47<ord(i)<59:
        m1+=i
for i in n:
    if 47<ord(i)<59:
        n1+=i

print(int(m1)+int(n1))