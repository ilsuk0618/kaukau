a, b, c, d=0, 0, 0, 0
for _ in range(3):    
    arr, arr2=input().split()
    if arr=='Y' and int(arr2)>=37:
        a+=1
    elif arr=='N' and int(arr2)>=37:
        b+=1
    elif arr=='Y' and int(arr2)<37:
        c+=1
    elif arr=='N' and int(arr2)<37:
        d+=1
if a>=2:
    print(a, b, c, d, "E")
else:
    print(a, b, c, d)