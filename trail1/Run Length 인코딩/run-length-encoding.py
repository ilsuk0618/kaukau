A=input()
cnt=1
B=[]
if len(A)==1:
    B.append(A[0])
    B.append(str(cnt))
    cnt=0
else:
    for i in range(1,len(A)):
        if A[i]==A[i-1] and 0<i<(len(A)-1):
            cnt+=1
        elif A[i]!=A[i-1] and i!=len(A)-1:
            B.append(A[i-1])
            B.append(str(cnt))
            cnt=1
        elif A[i]!=A[i-1] and i==len(A)-1:
            B.append(A[i-1])
            B.append(str(cnt))
            cnt=1
            B.append(A[i])
            B.append(str(cnt))
            cnt=0
        elif A[i]==A[i-1] and i==len(A)-1:
            cnt+=1
            B.append(A[i])
            B.append(str(cnt))
            cnt=0

for elem in B:
    for i in elem:
        cnt+=1
print(cnt)
for elem in B:
    print(elem,end="")