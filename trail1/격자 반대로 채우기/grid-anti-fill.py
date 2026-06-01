
##값을 규칙을 만들어 변화시키기 보다는 순차적으로 값을 늘려가되, 넣는 위치를 지정해주는 편이 낫다. 
n=int(input())

arr=[[0 for _ in range(n)]
for _ in range(n)
]

cnt=1

for col in range(n-1, -1, -1):
    if (n-1-col)%2==0:
        ##단순히 col값이 짝수, 홀수 인지를 보며 n 값에 따라서 감소해야하는곳이 달라진다. 그래서 경우를 n이 짝,홀수로 나눌수도 있지만 이는 코드를 두번 작성해야하기에 다른 조건을 잡아줘야함. 
        ##n-1,n-1은 무조건 1을 만들어야하기때문...
        for row in range(n-1, -1, -1):
            arr[row][col] = cnt
            cnt+=1
    else:
        for row in range(n):
            arr[row][col] = cnt
            cnt+=1

for elem in arr:
    for ans in elem:
        print(ans, end=" ")
    print()