text = input()
pattern = input()

def fin():
    i=len(text)
    j=len(pattern)
    cnt=-1
    for k in range(0,i-j+1):
        if text[k:k+j]==pattern[:]:
            cnt = k
            break
    if cnt==-1:
        return "-1"
    else:
        return cnt
print(fin())