i=int(input())

for j in range(i):
    if (j%2)==0 :
        print("*")
    else: 
        for h in range(j+1):
            print("*", end=" ")
        print()