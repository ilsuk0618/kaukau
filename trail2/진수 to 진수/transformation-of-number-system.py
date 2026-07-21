a, b = map(int, input().split())
n = input()

num=0
ans=[]

for i in range(len(n)):
    num = num*a+int(n[i])

while num>=b:
    ans.append(num%b)
    num//=b

ans.append(num)

for elem in ans[::-1]:
    print(elem,end="")
