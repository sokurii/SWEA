n = int(input())
paper = [[0] * 100 for _ in range(100)]

for _ in range(n):
    x,y = map(int,input().split())

    for i in range(10):
        for j in range(10):
            paper[100-x-i][y+j] += 1

    result = []
    for lst in paper:
        for i in lst:
            if i > 0:
                result.append(i)
print(len(result))
