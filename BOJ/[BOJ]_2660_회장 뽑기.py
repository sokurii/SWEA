n = int(input()) # 회장 후보 수
INF = 1e8
friend = [[INF]*(n+1) for _ in range(n+1)] # 친구 정보 배열
ans = []  # 회장 후보 점수 리스트

while True:
    a, b = map(int,input().split())
    if a == -1 and b == -1: # 입력 종료 조건
        break

    # 친구 점수
    friend[a][b] = 1
    friend[b][a] = 1

for i in range(1,n+1):
    friend[i][i] = 0

for k in range(1,n+1): # 친구의 친구
    for s in range(1,n+1):
        for e in range(1,n+1):
            friend[s][e] = min(friend[s][e],friend[s][k]+friend[k][e])

for i in range(1,n+1):
    mx = 0
    for j in range(1,n+1):
        if friend[i][j] != INF:
            mx = max(mx,friend[i][j])
    ans.append(mx)


mn = min(ans)
# 1. 후보 점수와 후보 수
print(mn,ans.count(mn))
# 2. 후보 인덱스(+1해주기)
for p in range(n):
    if ans[p] == mn:
        print(p+1, end=' ')


'''
조금 더 간결하게 풀고 싶다
'''











