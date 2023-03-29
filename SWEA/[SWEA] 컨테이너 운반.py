T = int(input())
for tc in range(1,T+1):
    w,t = map(int,input().split())

    # 화물 중량 : 최대로 싣기 위해 내림차순 정렬
    weight = sorted(list(map(int,input().split())))[::-1]
    # weight.sort(reverse=True)    sort로 정렬하는 방법도 있다

    # 적재용량
    truck = sorted(list(map(int,input().split())))[::-1]

    used = [0] * w              # 사용 화물 배열
    ans = 0

    for i in range(t):          # 트럭 적재 용량
        for j in range(i,w):    # 화물 중량
            # 사용하지 않았고 & 적재용량>화물중량이라면
            # 사용 후, 정답에 누적 (그렇지 않다면 그 다음 j(j+1)로 넘어감)
            if not used[j] and truck[i] >= weight[j]:
                used[j] = 1
                ans += weight[j]
                break           # 조건에 맞으면 화물 싣고 break(다음 i로 넘어감)
    # print(ans)

    # print(weight)
    # print(truck)
    print(f'#{tc} {ans}')

