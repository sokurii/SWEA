import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    age, name = input().split()
    lst.append((i,int(age),name))
    # lst.append((int(age),name))

lst.sort(key=lambda x:(x[1],x[0]))
# lst.sort(key=lambda x:x[0])

for user in lst:
    print(*user[1:])

'''
나이순으로 정렬을 하고, 나이가 같다면 입력순으로 출력

입력순서를 위해 따로 번호를 저장해서 리스트에 넣었는데
파이썬에서는 기본적으로 stable sort를 해서 그럴 필요가 없었다.

안정 정렬에서는 입력 받은 값들 중에 같은 값이 있는 경우 해당 값의 순서를 그대로 유지한다.
예를 들어, [1, 2, 3(X), 4, 5, 3(Y)] 을 오름차순 정렬한다면,
[1, 2, 3(X), 3(Y), 4, 5]순으로 세 번째 위치한 3의 위치와 여섯 번째 위치한 3의 위치가 바뀌지 않는다. 
unstalbe 정렬에서는 이러한 정렬을 장담할 수 없다.
파이썬은 기본적으로 stalbe 정렬을 한다는 점을 알아두면 좋다.'''

