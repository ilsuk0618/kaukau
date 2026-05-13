i=int(input())

for k in range(i):
    for h in range(k+1):
        print("*", end=" ")
    print()

for g in range(i-2,-1,-1):
    for h in range(g+1):
        print("*", end=" ")
    print()