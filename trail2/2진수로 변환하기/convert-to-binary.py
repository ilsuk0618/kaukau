n = int(input())
ans=[]
temp=0

while n>1:
    ans.append(n%2)
    n//=2

ans.append(n%2)

for elem in ans[::-1]:
    print(elem, end="")