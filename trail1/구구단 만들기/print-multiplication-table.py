##a,b 숫자 받는형식 잘 기억해두기. 
##두 숫자가 같을 경우 고려한거 굿. 
##/를 칠때 안칠때 구분하는 조건 너무 좋았다. 

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


    