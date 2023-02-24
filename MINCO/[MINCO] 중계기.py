'''
1. NxN 마을에 중계기(y,x) 설치
2. 집(hy,hx)을 모두 포함하는 중계기 반지름 R의 최소값
2-1. 집과 중계기 거리 D^2 = (hy-y)^2 + (hx-x)^2
2-2. D^2 <= R : 통신 범위에 포함
3. 시작점 (0,0)
'''

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    town = [list(map(int,input().split())) for _ in range(N+1)]

    # 중계기 위치
    r,c = 0,0
    for i in range(N+1):
        for j in range(N+1):
            if town[i][j] == 2:
                r,c=i,j

    # 집들의 위치
    home = []
    for i in range(N+1):
        for j in range(N+1):
            if town[i][j] == 1:
                home.append((i,j))

    # 거리
    d_lst = []
    for h in home:
        d = abs(h[0]-r)**2 + abs(h[1]-c)**2
        d_lst.append(d)

    R = 1
    while R**2 < max(d_lst):
        R +=1

    print(f'#{tc} {R}')






