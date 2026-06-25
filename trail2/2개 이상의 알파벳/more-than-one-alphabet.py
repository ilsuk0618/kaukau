A = input()

def alpha(A):
    arr=[0]*123
    cnt=0
    arr1=[]
    arr1.append(A)
    for elem in arr1:
        for i in elem:
            arr[ord(i)]+=1
    for elem in arr:
        if elem>=1:
            cnt+=1
    if cnt>=2:
        print("Yes")
    else:
        print("No")

alpha(A)

##아스키 코드를 사용하여 단어에있는 알파벳을 모두 식별 했지만 2개이상인지만 판단하는 문제이기에 서로다른 알파벳이 나오는지만 확인하는편이 간단하다.