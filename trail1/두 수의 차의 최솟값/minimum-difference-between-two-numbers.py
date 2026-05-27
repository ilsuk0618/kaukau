n=int(input())
arr=list(map(int, input().split()))
arr2=[]
arr2=arr
min_val=100

arr2.reverse()

for elem in arr2:
    for elem2 in arr:
        if elem!=elem2:
            if min_val>=(elem-elem2) and (elem-elem2)>0:
                min_val=(elem-elem2)

print(min_val)