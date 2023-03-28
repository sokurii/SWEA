def dfs(n):
    if n == N:
        print(*lst)
        return

    for i in range(1,N+1):
        if i not in lst:
            lst.append(i)
            dfs(n+1)
            lst.pop()

N = int(input())
lst = []
dfs(0)