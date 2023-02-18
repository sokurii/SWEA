T = 10

for tc in range(1,T+1):
    n = int(input()) # 문자열 길이
    text = input() # 문자열

    stack = []
    data = ''
    cal = []

    ## 후위 표기식으로 변환 ##
    for t in text:
        # 숫자면 push(저장)
        if t.isdigit():
            data += t
        # 더하기 연산자일 때
        elif not stack and t == '+': # 스택에 없으면 저장
            stack.append(t)
        elif stack and t == '+': #스택에 있으면 빼고 추가
            data += stack.pop() # 연산자 빠져
            stack.append(t)        # 다시 새로 넣어
    else:
        data += stack.pop()

    ## 결과값 계산 ##
    for i in data:
        # 숫자면 cal스택에 넣어
        if i != '+':
            cal.append(int(i))
        # 연산자면 스택에서 숫자 두 개 꺼내서 더하고 다시 넣어
        elif i == '+':
            num2 = cal.pop()
            num1 = cal.pop()
            cal.append(num1+num2)

    print(f'#{tc}',end=' ')
    print(*cal)