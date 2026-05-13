i=int(input())

for k in range(i):
    for j in range(i-k-1):
        print(end="  ")

    for h in range(2*k+1):
        print("*", end=" ")

    print()