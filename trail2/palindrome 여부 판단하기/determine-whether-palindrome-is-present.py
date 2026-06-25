A = input()

def pal(A):
    arr=[]
    arr2=[]
    arr.append(A)
    for elem in arr:
        for i in elem:
            arr2.append(i)
    arr3=[0*len(arr2)]
    arr3 = arr2[:]
    ##슬라이싱을 넣어줘야 2의 값이 온전히 3에 들어감. 슬라이싱을 하지 않는다면 2를 링크 걸어두는 격밖에 안됨
    arr2.reverse()
    if arr3 == arr2:
        print("Yes")
    else:
        print("No")

pal(A)