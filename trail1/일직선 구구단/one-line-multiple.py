i=int(input())

for k in range(1,i+1):
    for j in range(1,i+1):
        print(f"{k} * {j} = {j*k}", end="")
        print()