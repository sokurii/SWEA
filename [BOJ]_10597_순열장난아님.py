def dfs(n,s):
    global ans
    if n == len(lst)-1:
        print(*ans)
        return

    if lst[s] not in ans:
        if lst[s+1] == '0':
            lst[s] += lst.pop(s+1)
            ans.append(lst[s])
            dfs(n+1,s)
        ans.append(lst[s])
        dfs(n+1,s+1)


    else:
        lst[s] += lst.pop(s+1)
        dfs(n,s)

lst = list(input())
ans = []
dfs(0,0)


