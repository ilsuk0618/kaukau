arr=input().split()
##한줄에 주어지기 때문에 for로 10번 받는게 아니라 그냥 빈칸으로 구분하는 단어로 받느다. 
cnt=0
for elem in arr:
    cnt+=len(elem)
print(cnt)