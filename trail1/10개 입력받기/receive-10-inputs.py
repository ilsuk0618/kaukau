arr=map(int,input().split())
ans=0
arr2=[]
for elem in arr:
    if elem!=0:
        arr2.append(elem)
        ans+=elem
    else:
        break
if len(arr2)!=0:
    avg=ans/len(arr2)
else: avg=0

print(f"{ans} {avg:.1f}")