n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

ans=0
dat=["2200-00-00"]*n

for i in range(n):
    if weather[i]=="Rain":
        dat[i] = date[i]

min_val = dat[0]
for i in range(n):
    if min_val>=dat[i]:
        min_val = dat[i]
        ans = i


print(f"{date[ans]} {day[ans]} {weather[ans]}")