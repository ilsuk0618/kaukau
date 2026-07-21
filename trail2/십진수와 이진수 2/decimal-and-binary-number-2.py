N = input()
num=0
ans=[]

for i in range(len(N)):
    num = num*2+int(N[i])

num*=17

while num>=2:
    ans.append(num%2)
    num//=2

ans.append(num)

for elem in ans[::-1]:
    print(elem,end="")
