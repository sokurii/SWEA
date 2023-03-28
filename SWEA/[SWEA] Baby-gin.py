'''
[1] 플레이어 별로 카운팅 배열 생성해서 빈도수 체크
[2] baby-gin 체크  
'''

# baby_gin
def baby_gin(player, idx):
    # triplet
    if player[idx] == 3:
        return 1
    # run
    for i in (idx - 2, idx - 1, idx):
        if 0 <= i <= 7 and player[i] > 0 and player[i + 1] > 0 and player[i + 2] > 0:
            return 1

    # 둘 다 아니면 무승부
    return 0


T = int(input())
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    # 카운트 배열 생성
    player1 = [0] * 10
    player2 = [0] * 10

    ans = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            player1[lst[i]] += 1
            if baby_gin(player1, lst[i]):
                ans = 1
                break
        else:
            player2[lst[i]] += 1
            if baby_gin(player2, lst[i]):
                ans = 2
                break


    print(f'#{tc} {ans}')






