bingo = [list(map(int,input().split())) for _ in range(5)] # 빙고판
game = []   # 사회자가 부르는 빙고 번호
for _ in range(5):
    game.extend(list(map(int,input().split())))


for g in range(25):
    for i in range(5):
        for j in range(5):
            if game[g] == bingo[i][j]:
                bingo[i][j] = 0
                break



    cnt = 0
    # 가로 합
    for row in bingo:
        if sum(row) == 0:
            cnt += 1

    # 세로 합
    for m in range(5):
        col = 0
        for n in range(5):
            if bingo[n][m] == 0:
                col += 1
        if col == 5:
            cnt += 1

    # 대각선 합
    line1 = 0
    line2 = 0
    for k in range(5):
        if bingo[k][k] == 0:
            line1 += 1
        if bingo[k][4-k] == 0:
            line2 += 1
    if line1 == 5:
        cnt +=1
    if line2 == 5:
        cnt +=1


    if cnt >= 3:       # 3선 빙고 완성 조건
        print(game[g])
        break
