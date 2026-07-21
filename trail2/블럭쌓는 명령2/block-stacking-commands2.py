# 1234567
# 0123310이 되어
# 3개가 제일 많다고 출력

#0.칸의 개수, 명령하는 수를 받는다.
N,K = map(int, input().split())
#1.N개의 칸이 있도록 배열을 만든다. N=7 -> [00000000]
blocks = [0]*(N+1)
#2.명령받기
for _ in range(K):
    m,n = map(int, input().split())
    #m부터n까지 돌면서 칸에다가 1을 추가한다. 
    for j in range(m,n+1):
        blocks[j] +=1

#가장 큰 수 찾기
print(max(blocks))