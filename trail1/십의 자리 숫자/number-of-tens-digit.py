arr=list(map(int, input().split()))
arr_cnt=[0]*10

for elem in arr:
    if elem!=0:
        i=elem//10
        arr_cnt[i]+=1
    else:
        break

for k in range(1,10):
    print(f"{k} - {arr_cnt[k]}")