arr=['L','E','B','R','O','S']
ans=0
cnt=0
k=input()

for i in range(len(arr)):
    if arr[i] == k:
        if cnt==0:
            cnt+=1
            ans=i
        
if cnt==1:
    print(ans)
else:
    print('None')