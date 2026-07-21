n=int(input())
segment=[tuple(map(int, input().split())) for _ in range(n)]
line=[0]*101

for elem in segment:
    for i in range(elem[0],elem[1]+1):
        line[i]+=1

print(max(line))