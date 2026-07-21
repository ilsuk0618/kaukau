n = int(input())
segments = [tuple(input().split()) for _ in range(n)]
cnt=0
point=10000
line=[0]*20002
for elem in segments:
    if elem[1]=="R":
        for i in range(point,point+int(elem[0])):
            line[i]+=1
        point+=int(elem[0])
    else:
        for i in range(point-int(elem[0]),point):
            line[i]+=1
        point-=int(elem[0])
for k in line:
    if k>=2:
        cnt+=1
print(cnt)