i, k = map(int, input().split())

for j in range(i):
    for h in range(k):
        print((j+1)*(h+1), end=" ")

    print()

