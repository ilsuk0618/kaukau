i=int(input())
cnt=i
c=65

for j in range(i):
    for k in range(i-cnt,0,-1):
        print(" ", end=" ")

    for k in range(cnt):
        if c==90:
            print(chr(c), end=" ")
            c=65
            
        else:
            print(chr(c), end=" ")
            c+=1
        
    cnt-=1
    print()