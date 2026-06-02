i=input()
j=input()
arr=[]

for elem in i:
    if elem!= " ":
        print(elem, end="")
for elem in j:
    if elem!=" ":
        print(elem, end="")

##처음에는 arr 리스트에 빈칸이 아닌 단어를 추가 했었지만 그보다 그냥 바로 출력해버리면 됐다...