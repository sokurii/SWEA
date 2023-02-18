def paper(n):
    if n%10 == 0:
        if n == 10: # n=10 일 때 1 반환
            return 1
        elif n == 20: # n=20 일 때 2 반환
            return 3
        else:
            return paper(n-10) + paper(n-20)*2

T = int(input())
for tc in range(1,T+1):
    n= int(input())
    cnt = paper(n)
    print(f'#{tc} {cnt}')