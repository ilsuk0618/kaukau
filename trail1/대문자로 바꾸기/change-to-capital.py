arr=[list(map(ord, input().split()))
for _ in range(5)
]

for i in range(5):
    for k in range(3):
        if arr[i][k]>90:
            arr[i][k]-=32

##입력 문자가 모두 소문자이지 않은 경우를 고려해 아스키코드로 고려. 
##입력시 아스키 코드(ord)로, 출력시 문자(chr)로      
for i in range(5):
    for k in range(3):
        print(chr(arr[i][k]), end=" ")
    print()