a,b=map(int,input().split())
##두개의 정수를 각각 변수에 저장할때 
##띄워서 받는데 이것은 정수다. map해버려라
arr=[0]*10
ans=0
while a>1:
    c = a%b
    a = a//b
    arr[c] +=1
for k in range(10):
    if arr[k]!=0:
        ans = arr[k]**2+ans
 
print(ans)
