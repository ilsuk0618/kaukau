i=int(input())

for j in range(1,i+1,1):
    for k in range(1,i+1,1):
        print(f"{j} * {k} = {j*k}", end="")
        if k<i:
            print(",", end=" ")
    print()