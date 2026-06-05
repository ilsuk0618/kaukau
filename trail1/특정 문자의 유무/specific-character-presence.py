A=input()

cnt=0
for i in range(len(A)-1):
    if A[i]+A[i+1]=="ee":
        cnt=1
if cnt==1:
    print("Yes",end=" ")
else:
    print("No",end=" ")

cnt=0
for i in range(len(A)-1):
    if A[i]+A[i+1]=="ab":
        cnt=1
if cnt==1:
    print("Yes",end=" ")
else:
    print("No",end=" ")