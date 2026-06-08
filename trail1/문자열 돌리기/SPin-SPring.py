a=input()
n=len(a)

for _ in range(n+1):
    print(a)
    a = a[n-1]+a[0:n-1]
    