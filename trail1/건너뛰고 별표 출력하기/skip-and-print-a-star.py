i=int(input())

for k in range(i):
    for h in range(k+1):
        print("*", end="")
    print()
    print()

for j in range(i-1,-1,-1):
    for h in range(j):
        print("*", end="")
    print()
    print()