i=int(input())
sum_1=1
for k in range(i):
    arr = input().split()
    a, b = int(arr[0]), int(arr[1])

    for j in range(a,b+1):
        sum_1=sum_1*j
    
    print(sum_1)
    sum_1=1