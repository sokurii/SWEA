'''
수열 내에서도 오름차순이어야함
'''

N,M = map(int,input().split())
num = sorted(list(set(map(int,input().split()))))
ans = []

def dfs(n):
    if n == M:
        print(*ans)
        return

    for i in num:
        if n==0 or i >= ans[-1]:
            ans.append(i)
            dfs(n+1)
            ans.pop()
dfs(0)