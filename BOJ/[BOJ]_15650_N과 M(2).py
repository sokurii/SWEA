N, M = map(int,input().split())
lst = []    # 재귀함수에서 m개 수열을 저장할 리스트

def dfs(start):
    if len(lst) == M:   # 종료 조건 : 길이 == M
        print(*lst)
        return

    for i in range(start,N+1):
        if i not in lst:    # 리스트 중복 여부 확인
            lst.append(i)   # 중복이 아니면 리스트에 추가
            dfs(i)          # 현재 lst = [1] dls tkdghkddptj wornl
            lst.pop()       # [1] -> [1,2] -> [1] -> [1,3] .. 

dfs(1)





