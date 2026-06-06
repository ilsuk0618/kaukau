arr=input()
cnt1=0
cnt2=0

for i in range(len(arr)-1):
    if arr[i:i+2]=="ee":
        cnt1+=1
print(cnt1,end=" ")

for i in range(len(arr)-1):
    if arr[i:i+2]=="eb":
        cnt2+=1
print(cnt2)