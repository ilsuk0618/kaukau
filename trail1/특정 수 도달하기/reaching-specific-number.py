arr=list(map(int, input().split()))
arr2=[]
ans=0
avg=0
for elem in arr:
    if elem<250:
        arr2.append(elem)

    else:
        break
for ele in arr2:
    ans+=ele


avg=ans/len(arr2)

print(f"{ans} {avg:.1f}")
##소수 첫째 자리 까지 출력하려면 f-string 사용한다. 

