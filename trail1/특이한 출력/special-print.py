i=int(input())
cnt=0

for j in range(1,i+1):
    for k in range(1,i+1):      
        if cnt==1:
            print()
            print(f"({j}, {k})", end=" ")
            if (j+k)%4!=0:
                cnt-=1
            else:
                cnt=1                
        else:
            print(f"({j}, {k})", end=" ")
            if (j+k)%4==0:
                cnt+=1
                

      