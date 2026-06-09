arr=input()

for elem in arr:
    if 64<ord(elem)<91 or 96<ord(elem)<123 or 47<ord(elem)<58:
        print(elem.lower(), end="")