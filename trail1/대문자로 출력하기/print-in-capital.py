arr=input()
arr2=[]

for elem in arr:
    if 64<ord(elem)<91 or 96<ord(elem)<123:
        arr2.append(elem.upper())

for elem in arr2:
    print(elem, end="")