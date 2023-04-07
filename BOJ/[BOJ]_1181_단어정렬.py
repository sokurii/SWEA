N = int(input())
lst = []
for _ in range(N):
    lst.append(input())

lst = list(set(lst))  # set을 통해 중복 제거
lst.sort()
lst.sort(key=len)   # 리스트 값들의 길이에 따라 정렬해주기

for ans in lst:
    print(ans)

# for i in range(len(lst)-1):
#     for j in range(i,len(lst)):
#         if len(lst[i]) > len(lst[j]):
#             lst[i],lst[j] = lst[j],lst[i]

'''
set = 중복 제거
대신 순서가 없는 형태이기 때문에
for문이나 정렬 등 불가함 
-> list(set)으로 리스트로 바꿔주기
'''

'''
시간초과 오류 
=> lst.sort(key=len)   
리스트 값들의 길이에 따라 정렬하는 방법을 알게 됨 
'''
