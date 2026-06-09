arr=input()
cnt=0

for elem in arr:
    if 47<ord(elem)<58:
        cnt+=int(elem)
print(cnt)