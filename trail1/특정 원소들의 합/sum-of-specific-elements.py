arr=[list(map(int, input().split()))
for _ in range(4)
]

i=1
sum1=0

for k in range(4):
    for j in range(4):
        if j<i:
            sum1+=arr[k][j]
    i+=1

print(sum1)
        