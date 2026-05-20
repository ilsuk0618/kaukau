i=int(input())
cnt=1
c=65
for k in range(i):
    for j in range(cnt):
        if c==90:
            print(chr(c), end="")
            c=65
        else:
            print(chr(c), end="")
            c+=1
    cnt+=1
    print()