arr=[list(map(ord, input().split()))
for _ in range(5)
]

for i in range(5):
    for k in range(3):
        if arr[i][k]>90:
            arr[i][k]-=32
        
for i in range(5):
    for k in range(3):
        print(chr(arr[i][k]), end=" ")
    print()