T = int(input())

for tc in range(1,T+1):
    text = list(input())
    result = []

    for i in text:
        if len(result) == 0:
            result.append(i)
        elif len(result) != 0:
            if i == result[-1]:
                result.pop()
            else:
                result.append(i)
    print(f'#{tc} {len(result)}')
