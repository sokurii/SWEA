'''
- 근손실은 N일 동안 1일에 K 만큼 감소
- 현재 근력 - K + 중량 증가량 >= 0 이어야 함
'''
def dfs(depth, power):  # 깊이, 현재 체력
    global cnt

    # 깊이가 N이 되면 cnt +1 해주고 종료
    if depth == N:
        cnt += 1
        return

    for i in range(N):
        # 사용하지 않았고 & 근손실 없다면
        if not used[i] and power-K+lst[i]>=0:
            used[i] = 1 # 사용한 것 체크
            dfs(depth+1, power-K+lst[i])
            used[i] = 0 # 사용배열 초기화


N, K = map(int,input().split())
lst = list(map(int,input().split()))
cnt = 0
used = [0]*N

dfs(0,0)
print(cnt)