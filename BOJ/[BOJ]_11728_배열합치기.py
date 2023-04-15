'''
투포인터 연습
합친 배열은 오름차순 정렬로 나타내야 함
'''

a,b = map(int,input().split())
a_lst = list(map(int,input().split()))
b_lst = list(map(int,input().split()))
ans = []

# 인덱스 초기값 저장
ai, bi = 0, 0

# 인덱스가 범위 내에 있는 동안 비교하며 반복
while ai<a and bi<b:
    if a_lst[ai] <= b_lst[bi]:
        ans.append(a_lst[ai])
        ai += 1
    else:
        ans.append(b_lst[bi])
        bi += 1

while ai<a:
    ans.append(a_lst[ai])
    ai += 1
while bi<b:
    ans.append(b_lst[bi])
    bi += 1

print(*ans)

# 처음 잘못 짰던 코드
# ans = a_lst + b_lst
# end = 0
#
# for start in range(a+b):
#     while end < a+b:
#         if ans[start] > ans[end]:
#             ans[start],ans[end] = ans[end],ans[start]
#             end += 1
#     start -= 1
#
# print(ans)

'''
배열을 일단 합치고 투포인터로 정렬하는 문제인줄 알았는데
애초에 정렬되어 있는 두 배열의 인덱스를 0으로 설정 후 
각 배열의 값들을 투포인터로 비교하는 방법으로 풀어야 했다.

+) 비교를 하고 남은 리스트 요소의 경우 따로 조건에 따라 리스트 뒤에 추가해줘야 했다. 
'''