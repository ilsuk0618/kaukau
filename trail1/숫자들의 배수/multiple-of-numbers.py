i=int(input())
cnt=0
arr=[]
j=1
while cnt<=1:
    if i*j%5==0:
        cnt+=1
        arr.append(i*j)
        
    else:
        arr.append(i*j)
    j+=1

print(*arr)