i=int(input())
cnt=i
for k in range(1,i+1):
    for j in range(1,cnt+1):
        if j==cnt:
            print(f"{k} * {j} = {k*j}", end="")
            print()
        else:
            print(f"{k} * {j} = {k*j} / ", end="")

    cnt-=1