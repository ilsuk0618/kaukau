i=int(input())

for k in range(1,i+1,1):
    for h in range(1,k*2,1):
        if h<(k*2):
            print("*", end="")
        
    print()