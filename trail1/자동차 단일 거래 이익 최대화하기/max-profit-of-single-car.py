n = int(input())
price = list(map(int, input().split()))

max_val=0
i=0
for elem in price:
    for elem2 in price[i:n]:
        if max_val<=(elem2-elem):
            max_val=elem2-elem
    i+=1

print(max_val)