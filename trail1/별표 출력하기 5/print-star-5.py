i=int(input())
for k in range(i,0,-1):
    for h in range(k,0,-1):    
        for j in range(k):
            print("*", end="")
        print(end=" ")
    print()    
