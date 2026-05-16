##두 숫자를 각각이 아닌 한번에 입력받는 방식. 

i, k = map(int, input().split())

for j in range(i):
    for h in range(k):
        print((j+1)*(h+1), end=" ")

    print()

