'''
덩치 순위 : 자기보다 큰 사람의 수 + 1
튜플의 0번째, 1번째 요소 모두 커야 자기보다 크다고 할 수 있음!
애초에 cnt = 1을 초기값으로 설정하고, 큰 사람의 수를 더해주었다. 
'''

N = int(input())
lst = []
for _ in range(N):
    w,h = map(int,input().split())
    lst.append((w,h))

ans = []
for i in range(N):
    cnt = 1
    for j in range(N):
        if lst[i] != lst[j]:
            if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
                cnt += 1
    ans.append(cnt)
print(*ans)





