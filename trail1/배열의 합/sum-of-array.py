arr=[list(map(int, input().split()))
for _ in range(4)]
sum1=0
for i in range(4):
    sum1= sum(arr[i])
    print(sum1)