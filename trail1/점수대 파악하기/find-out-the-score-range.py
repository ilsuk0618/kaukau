arr=list(map(int, input().split()))
arr_cnt=[0]*11
for elem in arr:
    if elem!=0:
        k=elem//10
        arr_cnt[k]+=1
    else:
        break

for i in range(100,9,-10):
    print(f"{i} - {arr_cnt[i//10]}")