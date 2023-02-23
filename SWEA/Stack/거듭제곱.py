T = 10

for tc in range(1,T+1):
    tc =int(input())
    N, M = map(int,input().split()) # N의 M 거듭제곱 구하기

    result = N
    for _ in range(M-1):
        result *= N

    print(f'#{tc} {result}')
