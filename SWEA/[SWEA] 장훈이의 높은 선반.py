'''
만들 수 있는 높이가 B 이상인 탑 중에서
탑의 높이와 B의 차이가 가장 작은 것 출력
'''

def dfs(n,sm):
    global ans
    if n == N:
        if sm >= B:
            ans = min(ans,sm-B)
        return

    dfs(n+1,sm+H[n])    # 포함
    dfs(n+1,sm)         # 불포함


T = int(input())
for tc in range(1,T+1):
    N,B =map(int,input().split()) # 점원 수, 선반 높이
    H = list(map(int,input().split()))  # 점원 키 리스트

    ans = N * 10000         # ans = N * 최대 키 H

    dfs(0,0)

    print(f'#{tc} {ans}')