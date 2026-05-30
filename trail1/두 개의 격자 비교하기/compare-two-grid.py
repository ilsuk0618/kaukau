a,b=map(int, input().split())

arr1=[list(map(int, input().split())) for _ in range(a)]
arr2=[list(map(int, input().split())) for _ in range(a)]
arr3=[
    [0 for _ in range(b)] 
    for _ in range(a)
]

for i in range(a):
    for k in range(b):
        if arr1[i][k] == arr2[i][k]:
            arr3[i][k] = 0
        else:
            arr3[i][k] = 1

for i in range(a):
    for k in range(b):
        print(arr3[i][k], end=" ")
    print()