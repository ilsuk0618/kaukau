i=int(input())

for k in range(i):
    for j in range(k):
        print(" ", end=" ")
    for h in range(i-k,0,-1):
        print(h, end=" ")

    print()