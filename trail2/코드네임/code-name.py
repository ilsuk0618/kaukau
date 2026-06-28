MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))
class code:
    def __init__(self,name,sc):
        code.name=name
        code.sc=sc
code1 = code(codenames[0],scores[0])
code2 = code(codenames[1],scores[1])
code3 = code(codenames[2],scores[2])
code4 = code(codenames[3],scores[3])
code5 = code(codenames[4],scores[4])
cnt=0
min_val=100
for i in range(MAX_N):
    if min_val>=scores[i]:
        min_val=scores[i]
        cnt=i    

print(codenames[cnt], scores[cnt])