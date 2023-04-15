import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = 1e8
arr = [[INF]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int,input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = -1

for i in range(n):
    arr[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][k] == 1 and arr[k][j] == 1:
                arr[i][j] = 1
            elif arr[i][k] == -1 and arr[k][j] == -1:
                arr[i][j] = -1

for i in range(n):
    cnt = 0
    for j in range(n):
        if arr[i][j] == INF:
            cnt += 1
    print(cnt)
