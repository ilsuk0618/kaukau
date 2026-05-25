arr=list(map(int, input().split()))
i=-1
for elem in arr:
    if elem%3==0:
        break
    else:
        i+=1
print(arr[i])
