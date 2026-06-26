N = int(input())

def strip(a):
    if a==1:
        return 1
    if a==2:
        return 1

    return strip(a-1)+strip(a-2)


print(strip(N))