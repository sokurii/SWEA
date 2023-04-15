'''
시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = 1e8
fee = [[INF]*(n) for _ in range(n)]

for _ in range(m):
    start, end, cost = map(int,input().split())
    # 연결하는 노선은 하나가 아닐 수 있다.
    if cost<fee[start-1][end-1]:
        fee[start-1][end-1] = cost

for i in range(n):
    fee[i][i] = 0

for k in range(n):
    for s in range(n):
        for e in range(n):
            if fee[s][e] > fee[s][k] + fee[k][e] :
                fee[s][e] = fee[s][k] + fee[k][e]

for i in range(n):
    for j in range(n):
        # 만약 i에서 j로 갈 수 없는 경우 그자리에 0을 출력한다
        if fee[i][j] == INF:
            fee[i][j] = 0

for lst in fee:
    print(*lst)


'''
갈 수 없는 경우를 0으로 바꿔 주는 것을 간과하였다.
컴파일 에러 실수부터 출력초과, 시간초과, 틀렸습니다 까지 골고루 틀림 
'''