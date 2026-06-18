n = int(input())

def cal_0(n):
    num=0
    for i in range(n+1):
        num+=i
    num=num//10
    return num

num = cal_0(n)

print(num)