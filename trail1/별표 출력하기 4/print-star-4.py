i=int(input())

for k in range(i,0,-1):
    for h in range(k):    
        print("*", end=" ")
    print()

for k in range(2,i+1,1):
    for h in range(k):    
        print("*", end=" ")
    print()