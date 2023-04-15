n, k = map(int,input().split())
lst = list(map(int,input().split()))

end = 0
sm = 0
mx = 0

for start in range(n-k+1):
    while end < start+k and end < n:
        sm += lst[end]
        end += 1

    if mx == 0 or sm > mx:
        mx = sm
    sm -= lst[start]

print(mx)

