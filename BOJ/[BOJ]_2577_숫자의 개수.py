A = int(input())
B = int(input())
C = int(input())

# 자리수 하나씩 받기 위해 문자열로 바꾸고 리스트에 저장
mul = list(str(A*B*C))
# 인덱스별로 개수를 출력하기 위한 리스트
lst = [0]*10

for i in mul:
    lst[int(i)] += 1

for n in lst:
    print(n)




