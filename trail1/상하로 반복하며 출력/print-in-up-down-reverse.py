##가로줄로 봤을때 반복되는 것을 알 수 있다. 따라서 조건을 가로줄에 맞춰서 실행되는 코드를 다르게 하고 
##숫자변화를 만든다. 

i=int(input())
cnt=1
cnt1=i
for k in range(i):
    for j in range(i):
        if j%2==0:
            print(cnt,end="")
        
        else:
            print(cnt1,end="")
    print()
    cnt+=1
    cnt1-=1
