arr=list(map(str,input()))
c=len(arr)
arr[1]="a"
arr[c-2]="a"

for elem in arr:
    print(elem, end="")
