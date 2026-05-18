a, b = map(int, input().split())

if a==b:
    for k in range(1,10,1):
        print(f"{a} * {k} = {a*k}", end="")
        print()

else:
    for j in range(1,10,1):
        for k in range(b,a-1,-2):
            if k==a:
                print(f"{k} * {j} = {j*k}", end="")
            else:
                print(f"{k} * {j} = {j*k} /", end=" ")

        print()


    