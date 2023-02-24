'''
1. 1~N 자연수를 이진트리에 저장
2. 순회 순서는 중위순회(L-V-R)
3. 왼쪽은 i*2, 오른쪽은 i*2+1 이 될 것
4. num = 1을 시작으로 수를 늘려가며 트리에 저장/재귀(?)
5. 트리의 루트와 N/2 번 노드 출력 

=> 재귀로 순회하는 부분이 이해가 안 되어서 어려웠다..
'''


def inord(n):
    global num
    if n <= N:          # 노드 존재 조건
        inord(2*n)      # 왼쪽 서브트리 탐색 
        tree[n] = num   # 노드 방문 
        num += 1
        inord(2*n+1)    # 오른쪽 서브트리 탐색 

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)] # 노드 번호를 인덱스로 
    num = 1 
    inord(1)

    route = tree[1]                
    node = tree[N//2]

    print(f'#{tc} {route} {node}')



