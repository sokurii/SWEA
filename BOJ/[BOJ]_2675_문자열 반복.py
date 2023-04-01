N = int(input())
for _ in range(N):
    n, txt = input().split()

    ans = ''
    for s in txt:
        ans += int(n)*s

    print(ans)


