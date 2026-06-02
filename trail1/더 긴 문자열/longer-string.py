i,j=map(str, input().split())

if len(i)>len(j):
    print(i, len(i))
elif len(i)<len(j):
    print(j, len(j))
else:
    print('same')