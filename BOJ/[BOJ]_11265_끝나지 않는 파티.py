n, m = map(int,input().split())
stage = [[0]*(n+1)] + [[0] + list(map(int,input().split())) for _ in range(n)]

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            # stage[i][j] = min(stage[i][j], stage[i][k]+stage[k][j])
            if stage[i][j] > stage[i][k]+stage[k][j]:
                stage[i][j] = stage[i][k]+stage[k][j]

for _ in range(m):
    s,e,t = map(int,input().split())

    if stage[s][e] <= t:
        print('Enjoy other party')
    else:
        print('Stay here')


'''
시간초과 이슈로 min으로 구하는 부분을  값 크기 비교로 코드를 수정하였다 
플로이드 워셜 알고리즘은 노드가 500개 이하일 경우 적합하다는 점도 참고! '''