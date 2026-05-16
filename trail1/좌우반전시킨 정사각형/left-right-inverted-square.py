i=int(input())

for j in range(1,i+1,1):
    for h in range(i,0,-1):
        print(j*h, end=" ")
    print()