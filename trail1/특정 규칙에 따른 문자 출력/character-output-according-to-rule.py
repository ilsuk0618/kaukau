i=int(input())

for k in range(i):
    for j in range(i-k-1):
        print(end="  ")

    for h in range(k+1):
        print("@", end=" ")

    print()

for k in range(i):
    for j in range(i-k-1):
        print("@", end=" ")

    for h in range(k+1):
        print(end="  ")
    
    print()