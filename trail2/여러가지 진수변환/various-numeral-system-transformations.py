N, B = map(int, input().split())
ans=[]

while N>=B:
    ans.append(N%B)
    N//=B

ans.append(N)

for elem in ans[::-1]:
    print(elem,end="")
print()