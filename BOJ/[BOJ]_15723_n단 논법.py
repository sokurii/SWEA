N = int(input())
adj = [[] for _ in range(26)]
text = 'abcdefghijklmnopqrstuvwxyz'


def dfs(s):
    visited[s] = 1
    for i in adj[s]:
        if not visited[i]:
            dfs(i)
    return visited



# 전제 -> 인접행렬 처리
for _ in range(N):
    start,to = input().split(' is ')
    if start in text and to in text:
        start = text.index(start)
        to = text.index(to)
    adj[start].append(to)


M = int(input())
for _ in range(M):
    visited = [0] * 26
    left, right = input().split(' is ')
    if left in text and right in text:
        left = text.index(left)
        right = text.index(right)
    dfs(left)

    if visited[right] == 1:
        print('T')
    else:
        print('F')

'''
visited에서 굉장히 애를 먹었다. .
아직 그래프 더 풀어봐야 할듯. . 
플로이드–워셜으론 어떻게 푸는지.. 모릅니다.. .
'''





