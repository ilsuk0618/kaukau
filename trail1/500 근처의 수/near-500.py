arr=list(map(int, input().split()))
max_val=0
min_val=1000

for elem in arr:
    if elem>=max_val and elem<500:
        max_val=elem
    elif elem<=min_val and elem>500:
        min_val=elem
print(max_val, min_val)