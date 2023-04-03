'''
풀고자라 진순이
'''
n = int(input())
a,b = map(int,input().split())
m = int(input())

adj = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split()) # x:부모 ,y:자식
    adj[x].append(y)
    # adj[y].append(x)
print(adj)