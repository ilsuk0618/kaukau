i=int(input())

for k in range(2*i+1):
    if k%2==0:
        for j in range(2*i+1):
            print("*", end=" ")

    else:
        for j in range(i+1):
            print("*   ", end="")
    
    print()