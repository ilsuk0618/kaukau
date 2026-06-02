i=input()
j=input()
arr=[]

for elem in i:
    if elem!= " ":
        arr.append(elem)
for elem in j:
    if elem!=" ":
        arr.append(elem)

for elem in arr:
    print(elem, end="")