'''
백트래킹
: 가능한 모든 경우를 실행해 정답을 찾는다

- n : 선택한 숫자의 개수(길이)
- n = 0 부터 시작해 개수 세기
- if n == M: 종료
- dfs(n, .. , ..) 첫 파라미터는 종료조건 넣어주기
'''

N, M = map(int,input().split())
ans = []
visited = [0]*(N+1)

def dfs(n,lst):
    # 종료조건처리(n관련) + 정답 처리
    if n == M: # 길이가 M인 수열이 완성된다면
        ans.append(lst)
        return

    # 하부처리(함수)
    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = 1
            dfs(n+1,lst+[i])
            visited[i] = 0

dfs(0,[])
for lst in ans:
    print(*lst)