i=int(input())

for k in range(i):
    for h in range(i-k-1,0,-1):
        print(end=" ")
    for j in range(k+1):
        print("*", end=" ")

    print()

for k in range(i,1,-1):
    for h in range(i-k+1,0,-1):
        print(end=" ")
    for j in range(k-1):
        print("*", end=" ")

    print()