i=int(input())

for k in range(i,0,-1):
    for h in range(2):
        for j in range(k):
            print("*",end="")
        
        for j in range(i-k):
            print(end="  ")

    print()