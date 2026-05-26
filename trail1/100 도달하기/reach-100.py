i=int(input())
p3=2
arr=[]

arr.append(1)
arr.append(i)

while arr[p3-1]<=100:
    arr.append(0)
    arr[p3]=arr[p3-1]+arr[p3-2]
    
    p3+=1
print(*arr)
