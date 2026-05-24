arr=map(int,input().split())
arr2=[]
for elem in arr:
    if elem==0:
        break

    else:
        arr2.append(elem)

arr2.reverse()
print(*arr2)
##list 뒤집는 함수, 리스트에 쉼표와 괄호 없이 예쁘게 나오게 하는 "*"