n = int(input())

def type(n):
    if n==0:
        return

    type(n-1)
    print(n, end=" ")
     ##재귀함수 속 프린트 위치의 중요성...굳이 처음에 1넣고 하나씩 늘리지 않아도 프린트위치만 조절해도 n 바로 넣어도 됨.
def type2(n):
    if n==0:
        return

    print(n, end=" ")
    type2(n-1)

type(n)
print()
type2(n)
