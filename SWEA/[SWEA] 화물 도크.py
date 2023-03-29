'''
회의가 가장 빨리 끝나는 순으로 정렬
종료 시간이 같을 경우 시작 시간이 빠른 순으로 정렬
겹치지 않는지 확인
'''

T = int(input())
for tc in range(1,T+1):
    N =int(input())
    lst = []
    for _ in range(N):
        s,e = map(int,input().split())
        lst.append((e,s))   # 종료시간, 시작시간

    # 종료시간 빠른 순으로 정렬
    lst.sort()
    # print(lst)

    end = 0
    cnt = 0
    for e, s in lst:
        if s >= end:     # 현재 시작시간이 이전 종료시간보다 늦으면 카운트
            cnt += 1
            end = e      # 종료시간 재설정

    print(f'#{tc} {cnt}')


