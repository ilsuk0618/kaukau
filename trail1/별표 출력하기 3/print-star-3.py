i=int(input())

for k in range(i,0,-1):
    for j in range(i-k):
        print(end="  ")
    
    for h in range(2*k-1):
        print("*", end=" ")
    print()