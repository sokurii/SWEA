def count(ground):
    max_v = 2 # 최소길이
    for lst in ground:
        cnt = 0
        for i in lst:
            if i==1: # 1이 연속해서 존재하면 +=1
                cnt+=1
                if max_v<cnt:
                    max_v = cnt
            else: # 아니라면 cnt 초기화
                cnt=0
    return max_v


T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for tc in range(1,T+1):
    N,M = map(int,input().split())
    ground_row = [list(map(int,input().split())) for _ in range(N)]
    ground_col = list(map(list, zip(*ground_row)))

    row = count(ground_row)
    col = count(ground_col)
    if row<col:
        row = col

    print(f'#{tc} {row}')