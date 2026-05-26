i=int(input())
p=1
p2=i
p3=2
arr=[]

arr.append(p)
arr.append(p2)
arr.append(0)

while arr[p3-1]<=100:
    arr[p3]=arr[p3-1]+arr[p3-2]
    k=arr[p3]
    arr.append(k)
    p3+=1
arr.pop()
print(*arr)
