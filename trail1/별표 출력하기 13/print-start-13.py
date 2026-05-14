i=int(input())

for k in range(2*i):
    if k%2==0 :
        for j in range(i-(k//2)):
            print("*", end=" ")

    else:
        for j in range((k//2)+1):
            print("*", end=" ")
    
    print()