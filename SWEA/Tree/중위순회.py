'''
주어진 트리를 in-order 형식으로 순회할 때 나오는 단어 출력
1. 0으로 된 리스트(tree) 만들기
2. 입력값을 리스트로 저장(lst)
2-1. 리스트 0번째 값은 tree의 인덱스
2-2. 리스트 1번째 값은 tree의 값들로 저장
3. 중위순회 함수 만들기
3-1. 함수를 L-V-R로 순회하며 재귀
3-2. tree[n]의 값을 word 문자열에 +=
4. 이어 붙여진 단어(word) 출력

'''
def inord(n):
    global word
    if n <= N:
        inord(2*n)
        word += tree[n]
        inord(2*n+1)

T = 10
for tc in range(1,T+1):
    N = int(input())
    tree = [0 for _ in range(N + 1)]
    for i in range(N):
        lst = list(input().split())
        tree[i+1] = lst[1]
    word = ''
    inord(1)
    print(f'#{tc} {word}')