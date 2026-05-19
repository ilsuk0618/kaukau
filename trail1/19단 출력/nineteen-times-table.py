cnt=0

for i in range(1,20):
    for k in range(1,20):
        if cnt==0:
            print(f"{i} * {k} = {i*k} ", end="")
            if k%2==0:
                cnt+=1
            else:
                print("/", end=" ")
        else:
            print()
            if k==19:
                print(f"{i} * {k} = {i*k}", end=" ")
                cnt=0
            else:
                print(f"{i} * {k} = {i*k} /", end=" ")
                cnt=0
    print()

