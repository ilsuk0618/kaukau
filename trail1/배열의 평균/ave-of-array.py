arr = [list(map(int, input().split()))
for n in range(2)
]
sum1=0
avg_1=0
avg_2=0

for i in range(2):
    for k in range(4):
        sum1 += arr[i][k]
    avg_1=sum1/4
    print(f"{avg_1:.1f}", end=" ")
    sum1=0
print()
t=0
for _ in range(4):
    for i in range(2):
        for k in range(t,t+1):
            sum1 += arr[i][k]
    avg_2=sum1/2
    print(f"{avg_2:.1f}", end=" ")
    sum1=0         
    t+=1
print()

print(f"{(sum(arr[0])+sum(arr[1]))/8:.1f}")
