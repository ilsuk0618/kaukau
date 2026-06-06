arr=input()
a=input()
cnt=0

for i in range(len(arr)-1):
    if arr[i:i+2]==a:
        cnt+=1
print(cnt)