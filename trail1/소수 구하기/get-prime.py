i=int(input())
for j in range(1,i+1):
    cnt=0
    for k in range(1,j+1):
        if j%k==0:
            cnt+=1
    
    if cnt==2:
        print(j, end=" ")