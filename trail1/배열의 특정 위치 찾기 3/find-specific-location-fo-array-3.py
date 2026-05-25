arr=list(map(int, input().split()))
arr2=[]
ans=0
for elem in arr:
    if elem==0:
        break
    else:
        arr2.append(elem)
for i in range(len(arr2)-1,len(arr2)-4,-1):
    ans+=arr2[i]

print(ans)