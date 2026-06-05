arr=input()
arr2=[]

for i in range(len(arr)):
    if i%2!=0:
        arr2.append(arr[i])
arr2.reverse()

for elem in arr2:
    print(elem, end="")