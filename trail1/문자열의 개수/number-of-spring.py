cnt=0
arr=[]
while True:
    m=input()
    if m!="0":
        cnt+=1
        if cnt%2!=0:
            arr.append(m)
    else:
        break
print(cnt)
for elem in arr:
    print(elem)