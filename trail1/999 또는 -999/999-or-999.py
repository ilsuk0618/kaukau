a=list(map(int, input().split()))
min_val=a[0]
max_val=a[0]

for elem in a:
    if elem==999 or elem==-999:
        break
    elif elem>=max_val:
        max_val=elem
    elif elem<=min_val:
        min_val=elem
    
print(max_val, min_val)