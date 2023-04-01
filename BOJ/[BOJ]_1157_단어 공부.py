'''
[1] 입력값 : 대소문자 혼합, 출력값 : 대문자
=> .upper() 이용하여 대문자로 바꿔주기

[2] 딕셔너리로 풀면 편할 것 같은데.. 공부해
=> 예시 코드
dict = {}
for i in input_data:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

느낀 점 : 더 쉽게 풀 수 있을 것 같은데..
'''

# 입력값 대문자로 바꾸기
word = input().upper()
dic = {}

# 딕셔너리 만들기
for t in text:
    if t not in dic:
        dic[t] = 1
    else:
        dic[t] += 1

# 단어 속 최빈값
mx = max(dic.values())  # 딕셔너리 values 중 최대값

# 최빈값이 2개 이상일 경우 ? 출력,
# 1개일 경우 그 값의 key 출력
ans = []
for i in dic:
    if dic[i] == mx:
        ans.append(i)
if len(ans) > 1:
    print('?')
else:
    print(*ans)






