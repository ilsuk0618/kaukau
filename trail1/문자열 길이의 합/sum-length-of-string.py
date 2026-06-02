n=int(input())
arr=[input()
for _ in range(n)]

ln=0
cnt=0

for elem in arr:
    ln+=len(elem)
    if elem[0]=="a":
        cnt+=1

print(ln, cnt)