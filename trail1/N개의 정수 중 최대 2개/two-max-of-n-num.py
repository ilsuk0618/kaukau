n = int(input())
a = list(map(int, input().split()))

max_val=a[0]
min_val=a[0]
cnt=0
cnt1=0

for i in range(n):
    if a[i] >= max_val:
        max_val=a[i]
        cnt=i
    elif a[i] <= min_val:
        min_val=a[i]
        cnt1=i
a[cnt]=a[cnt1]
max_val2=min_val

for i in range(n):
    if max_val2<=a[i] and max_val2<=max_val:
        max_val2=a[i]

print(max_val, max_val2)