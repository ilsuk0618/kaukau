i=int(input())

for k in range(i):
    if k==0 or k==i-1:
        for j in range(i):
            print("*", end=" ")
        print()

    else:
        for h in range(i):
            if h==i-1:
                print("*", end=" ")
            
            elif h<k :
                print("*", end=" ")

            else:
                print(end="  ")
            
        print()