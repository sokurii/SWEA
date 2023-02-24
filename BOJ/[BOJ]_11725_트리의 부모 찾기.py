'''
1. 자식 노드들의 부모를 구하는 문제 (자식 노드를 인덱스로 하는 부모 리스트(p_lst) 만들기)
2. 노드 간 연결 관계를 인접 리스트에 저장(인덱스:부모, 값:자식)
3. 트리의 루트인 1부터 시작.
3-1. 인접리스트에 값들(자식 노드)이 있고
3-2. 그 값들이 부모 리스트에 없다면
3-3. 부모 리스트의 자식 인덱스에 부모 노드 저장
4. 2번 노드부터 순서대로 출력

=> 헷갈려서 완벽히 이해하기 어려웠다. 다시 풀기..
=> 시간초과로 pypy로 내버렸다.
'''
N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    start, to = map(int,input().split())
    adj[start].append(to)
    adj[to].append(start)

p_lst = [0] * (N + 1)
q = []
q.append(1) # 트리 루트인 1부터 순회

def bfs():
    while q:
        t = q.pop(0)
        for nt in adj[t]:
            if not p_lst[nt]:
                p_lst[nt] = t
                q.append(nt)

bfs()

for p in p_lst[2:]:
    print(p)








