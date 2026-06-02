i=input()
j=input()
k=input()
arr=[]
arr.append(i)
arr.append(j)
arr.append(k)

max_val=0
min_val=20 
for _ in range(2):
    for elem in arr:
        if len(elem)>max_val:
            max_val=len(elem)
        elif len(elem)<min_val:
            min_val=len(elem)
print(max_val-min_val)
