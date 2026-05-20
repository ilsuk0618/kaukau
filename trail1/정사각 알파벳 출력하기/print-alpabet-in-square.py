i=int(input())
cnt=65
for j in range(i):
    for k in range(i):
        if cnt==90:
            print(chr(cnt), end="")
            cnt=65
        
        else:
            print(chr(cnt), end="")
            cnt+=1
    print()