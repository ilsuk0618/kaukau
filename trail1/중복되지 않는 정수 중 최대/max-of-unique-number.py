a=int(input())
nums = list(map(int, input().split()))
arr=[0]*1001
max_val=-1
cnt=1000
for elem in nums:
    arr[elem]+=1
arr.reverse()
for a in arr:
    if a==1 :
        max_val=cnt
        break
    else:
        cnt-=1
    
print(max_val)
