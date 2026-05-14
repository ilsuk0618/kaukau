##짝수인지 홀수인지에 관계가 있겟구만. 이건 그림은 가로로 봤을때나 가능. 세로로 봐야하기에 좌표처럼 생각해보자.  

i=int(input())

for k in range(i):

    if k==0:
        for j in range(i):
            print("*", end=" ")
    
    else:
        for p in range(i):
            if p%2!=0 and p>=k:
                print("*", end=" ")
            else:
                print(end="  ")
         

    print()