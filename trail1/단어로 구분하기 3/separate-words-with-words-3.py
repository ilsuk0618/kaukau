arr=[input().split()]
##문자를 입력 받을때 괄호를 안쓰고, input().split()해도 리스트로 저장됨. 지금처럼 괄호를 쓰고 받으면 그냥 전체에 껍데기 하나 더 씌우는 꼴...
for elem in arr:
    elem.reverse()
    for ans in elem:
        print(ans)