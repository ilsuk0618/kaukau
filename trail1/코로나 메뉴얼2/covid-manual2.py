a, b, c, d=0, 0, 0, 0
for _ in range(3):    
    arr=list(map(str,input().split()))
    ##지금 변수 두개에 받은것은 정수가 아니라 문자열로 받았기 때문에 
    ##숫자로 비교하고 싶다면 , int로 변환해줘야한다. 
    ##추가적으로 문자열 형태로 리스트로 받아서 비교해봄.
    if arr[0]=='Y' and int(arr[1])>=37:
        a+=1
    elif arr[0]=='N' and int(arr[1])>=37:
        b+=1
    elif arr[0]=='Y' and int(arr[1])<37:
        c+=1
    elif arr[0]=='N' and int(arr[1])<37:
        d+=1
if a>=2:
    print(a, b, c, d, "E")
else:
    print(a, b, c, d)