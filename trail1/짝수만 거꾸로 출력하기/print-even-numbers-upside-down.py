num=int(input())
arr=map(int, input().split())
arr2=[]
for elem in arr:
    if elem%2==0:
        arr2.append(elem)

print(*arr2[::-1])        