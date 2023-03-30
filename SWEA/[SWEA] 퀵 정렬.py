# quickSort(리스트, 시작 인덱스(0), 끝 인덱스(len(lst)-1))
def quickSort(lst,start,end):
    if start >= end:
        return

    # 비교할 인덱스 지정
    pivot = start       # 피봇 = 시작 인덱스
    left = start+1      # left = 그 다음 인덱스
    right = end         # right = 끝 인덱스

    # 엇갈릴 때까지 반복
    while left <= right:
        # [1] 선형 탐색
        # 피벗보다 큰 데이터 찾을 때까지 왼->오 이동
        while left <= end and lst[left] <= lst[pivot]:
            left += 1
        # 피벗보다 작은 데이터 찾을 떄까지 오->왼 이동
        while right > start and lst[right] >= lst[pivot]:
            right -= 1

        # [2] 자리 바꾸기
        # 왼(큰값)/오(작은값) 찾으면 자리 교체
        if left <= right:
            lst[left], lst[right]  = lst[right], lst[left]
        # 왼/오 엇갈리면(큰 값이 더 오른쪽에 있다면)
        # 작은 값 <-> 피벗 교체
        elif left > right:
            lst[right], lst[pivot] = lst[pivot], lst[right]

    # [3] 정렬 수행
    # 분할 이후 왼/오 에서 다시 각각 정렬 수행
    quickSort(lst,start,right-1)
    quickSort(lst,right+1, end)




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    # print(lst)

    quickSort(lst,0,len(lst)-1)
    print(f'#{tc} {lst[N//2]}')
