i=int(input())

for k in range(i-1,-1,-1):
    for h in range(i-k-1):
        print(end="  ")
    
    for j in range(k*2+1):
        print("*",end=" ")
    
    print()

for k in range(1,i,1):
    for h in range(i-k-1):
        print(end="  ")
    
    for j in range(k*2+1):
        print("*",end=" ")
    
    print()
