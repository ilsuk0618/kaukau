## 홀수줄은 1씩 증가하는 수열, 짝수줄은 1씩 감소하는 수열
i=int(input())

for k in range(2*i):
    if (k%2==0):
        for j in range(1+(k//2)):
            print("*", end=" ")

    else:
        for j in range((i-(k-1)//2)):
            print("*", end=" ")
        
    print()
