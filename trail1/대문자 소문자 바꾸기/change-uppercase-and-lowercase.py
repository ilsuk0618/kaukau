arr=input()

for elem in arr:
    if 64<ord(elem)<91: 
        print(elem.lower(), end="")
    elif 96<ord(elem)<123:
        print(elem.upper(), end="")