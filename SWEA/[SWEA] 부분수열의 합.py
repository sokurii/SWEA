'''
백트래킹 : 가능한 모든 경우(트리)를 탐색하여 답을 찾아냄
* 시간초과 가능, 복잡도를 미리 검토한다.
[1] 종료조건(n)
    n : 숫자번호(idx)
[2] tree 시각적 표현

N개의 자연수가 주어졌을 때 합이 K가 되는 경우의 수
'''
def dfs(n,sm):
    global cnt
    # [3] 가지치기 : 더 이상 갱신 가능성 없는 경우
    # 가장 마지막에, 가장 위쪽에
    if K < sm:
        return

    # [1] 종료조건(n관련)
    if n == N:
        if sm == K:
            cnt += 1
        return

    # [2] 하부호출
    dfs(n+1,sm+lst[n])  # 포함 o
    dfs(n+1, sm)        # 포함 x



T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    lst = list(map(int,input().split()))

    cnt = 0
    dfs(0,0)

    print(f'#{tc} {cnt}')