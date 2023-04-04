N = int(input())
num = N
lst = []

while True:
    if num == 0:
        break
    # num을 하나씩 줄여가면서 분해합을 구한다
    num -= 1
    num_str = str(num)
    sm = 0  # 각 자리수를 더할 변수

    # 문자열로 받아 쪼갠 뒤 합을 구함
    for i in num_str:
        sm += int(i)

    # 분해합 조건이 충족되었을 때 가능한 생성자 리스트에 저장
    if num + sm == N:
        lst.append(num)

if len(lst) == 0:
    print(0)
else:
    print(min(lst))

'''
분해합과 생성자를 생각해내는 데 시간이 조금 걸렸다.
다른사람들의 풀이가 간결했는데 참고해보자면..
'''
'''
n = int(input())
for i in range(1,n+1):  # 1부터 입력값까지
    num = sum(map(int,str(i)))  # 분해된 각 자리수 합
    num_sum = i + num  # 분해합 = 생성자 + 각 자리수 합

    # ** i가 작은 수부터 차례로 들어가기 때문에
    # 처음으로 분해합 = 입력값 같을 때가 가장 작은 생성자를 가진다
    if num_sum == n:
        print(i)
        break
    if i == n:      # ex)1, 생성자 i와 입력값이 같다는 것은 생성자가 없다는 뜻 
        print(0)
'''








