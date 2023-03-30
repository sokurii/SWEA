T = int(input())

def mergeSort(lst):
    # [1] 종료 조건
    if len(lst) ==1:
        return lst

    # [2] 분할
    # 가운데 기준으로 왼/오
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    # [3] 정복
    left = mergeSort(left)
    right = mergeSort(right)

    # [4] 합병
    # 왼+오 합친 결과 return
    return merge(left,right)


# 병합 함수
def merge(left,right):
    global cnt
    # 합병하기 전 왼쪽 마지막 원소, 오른쪽 마지막 원소 비교
    # 왼쪽이 더 큰 경우 cnt +1
    if left[-1] > right[-1]:
        cnt += 1

    # 왼, 오 각각 꺼내올 인덱스 선언
    li = ri = 0

    # 결과 담을 리스트
    result = []
    # 왼, 오 둘 중 하나라도 원소 있는지 확인
    while li < len(left) or ri < len(right):
        # 왼, 오 둘 다 원소 있으면 작은 것 부터 리스트에
        if li < len(left) and ri < len(right):
            if left[li] <= right[ri]:
                result.append(left[li])
                li += 1
            else:
                result.append(right[ri])
                ri += 1
        # 왼쪽만 남았다면 왼쪽 다 담기
        elif li < len(left):
            result.append(left[li])
            li += 1
        # 오른쪽만 남았다면 오른쪽 다 담기
        elif ri < len(right):
            result.append(right[ri])
            ri += 1
    return result


for tc in range(1,T+1):
    N = int(input())
    sort_list = list(map(int,input().split()))
    cnt = 0

    sorted_list = mergeSort(sort_list)

    print(f'#{tc} {sorted_list[N//2]} {cnt}')