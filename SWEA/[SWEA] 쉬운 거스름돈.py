T = int(input())
money = [50000,10000,5000,1000,500,100,50,10]
cnt = []

for tc in range(1,T+1):
    n = int(input())
    cnt = []

    for m in money:
        cnt.append(n // m)
        n = n%m

    print(f'#{tc}')
    print(*cnt)


