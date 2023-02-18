T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]

    for i in range(n):
        arr[i][0] = 1 # 0열은 무조건 1 
        for j in range(1,n):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{tc}')
    for i in range(n): 
        print(*arr[i][:i+1]) # 리스트 속 0 제거 