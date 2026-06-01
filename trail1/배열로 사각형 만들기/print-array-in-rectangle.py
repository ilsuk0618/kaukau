arr=[[0 for _ in range(5)]
for _ in range(5)
]

for i in range(5):
    for j in range(5): 
        if i==0: 
            arr[0][j] = 1
        elif j==0:
            arr[i][0] =1
        elif i!=0 and j!=0:
            arr[i][j]=arr[i-1][j]+arr[i][j-1]

for elem in arr:
    for ans in elem:
        print(ans, end=" ")
    print()