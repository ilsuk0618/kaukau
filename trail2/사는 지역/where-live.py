n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

name1=name[0]
cnt=0
ans=0
for elem in name:
    cnt+=1
    if name1<=elem:
        name1=elem
        ans = cnt
print(f"name {name[ans-1]}")
print(f"addr {street_address[ans-1]}")
print(f"city {region[ans-1]}")