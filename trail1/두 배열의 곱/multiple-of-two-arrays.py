arr1=[list(map(int, input().split())) for _ in range(3)
]
input()
## 공백을 주기에 고려하면서 받기. 
arr2=[list(map(int, input().split())) for _ in range(3)
]
ans=0

for i in range(3):
    for j in range(3):
        ans = arr1[i][j] * arr2[i][j]
        print(ans, end=" ")
    print()