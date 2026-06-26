N = int(input())


## 종료조건을 1,2일 때 각각을 적는 이유는 8번째를 구하기위해서는 점화식을 N-1,N-2를 더한다로 적기때문에 8->1순으로 역으로 항을 구해가는과정을 거치기 때문인다. 
def strip(a):
    if a==1:
        return 1
    if a==2:
        return 1

    return strip(a-1)+strip(a-2)


print(strip(N))