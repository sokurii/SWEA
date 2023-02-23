# 서브트리 (자식1, 자식2) 풀이
'''
부모  # 1 2 3 4 5 6
자식1 # 6 1 0 0 3 4
자식2 # 0 5 0 0 0 0
'''
def subtree(n):
    global cnt
    if n == 0:
        return
    cnt += 1
    subtree(c1[n])
    subtree(c2[n])


T = int(input())
for tc in range(1,T+1):
    E,N = map(int,input().split())
    tree = list(map(int,input().split())) # E*2개 요소

    # *E+2 : 0과 마지막 범위 포함
    c1 = [0] * (E+2)
    c2 = [0] * (E+2)

    for i in range(E):
        p,c = tree[i*2], tree[i*2+1] # p:부모 c:자식
        if not c1[p]:
            c1[p] = c
        else:
            c2[p] = c

    cnt = 0
    subtree(N)
    print(f'#{tc} {cnt}')


'''
단순히 내가 아는 bfs로 풀긴 했는데
부모 노드를 인덱스로 하는 이진트리 (자식1,자식2)를
구현하는 방법을 다른사람들 코드를 통해 알게되었다..
'''



'''
T = int(input())
for tc in range(1,T+1):
    E,N = map(int,input().split())
    tree = list(map(int,input().split()))

    adj = [[] for _ in range(E+2)]
    for i in range(E):
        start = tree[2*i]
        to = tree[2*i+1]
        adj[start].append(to)
    # print(adj)

    visited = [0 for _ in range(E+2)]
    visited[N] = 1
    q = []
    q.append(N)

    cnt = 1
    while q:
        t = q.pop(0)

        for nt in adj[t]:
            if not visited[nt]:
                q.append(nt)
                cnt += 1


    print(f'#{tc} {cnt}')
    
'''
