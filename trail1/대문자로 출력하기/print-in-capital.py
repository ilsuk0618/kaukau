arr=input()

for elem in arr:
    if 64<ord(elem)<91 or 96<ord(elem)<123:
        print(elem.upper(), end="")