'''
왕복 사이클의 최소 도로 합 구하기 (cycle[i][i]의 최솟값)
'''
import sys
input = sys.stdin.readline

V, E = map(int,input().split())
INF = 1e8
cycle = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a,b,c = map(int,input().split())
    cycle[a][b] = c     # 단방향

# 플로이드 워셜
for k in range(1,V+1):
    for s in range(1,V+1):
        for e in range(1,V+1):
            cycle[s][e] = min(cycle[s][e], cycle[s][k]+cycle[k][e])

# 최솟값 구할 때 큰 값과 비교해주기
mn = INF
for a in range(1,V+1):
    mn = min(mn,cycle[a][a])

if mn == INF:
    print(-1)
else:
    print(mn)


'''
실수 : 자기 자신 도로 길이는 0 (X)
자기 자신 -> 자기 자신 즉, 왕복 거리를 계산하는 문제 

따라서 
for i in range(1,V+1):
cycle[i][i] = 0 이렇게 해주면 안된다! 
=> 구하고자 하는 값이 cycle[i][i]의 최솟값임  
'''

'''
시간초과 -> pypy 제출
python으로 풀려면 다익스트라 알고리즘으로 풀어야 함 
'''
# cnt = 0
# for i in range(1,V+1):
#     for j in range(1,V+1):
#         if cycle[i][j] != INF:
#             cycle[i][j] = 0
#
#         if cycle[i][j] != 0 and cycle[j][i] != 0:
#             cnt = cycle[i][j]+cycle[j][i]
#
# if cnt != 0:
#     print(cnt)
# else:
#     print(-1)









