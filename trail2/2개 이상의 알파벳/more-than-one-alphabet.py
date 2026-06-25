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