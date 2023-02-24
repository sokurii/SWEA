def inord(n):
    global num
    if n <= N:
        inord(2*n)
        tree[n] = num
        num += 1
        inord(2*n+1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree=[0 for _ in range(N+1)]
    num = 1
    inord(1)

    route = tree[1]
    node = tree[N//2]

    print(f'#{tc} {route} {node}')