arr=input()
a=list(arr)
c=len(arr)
a[1]="a"
a[c-2]="a"

for elem in a:
    print(elem, end="")