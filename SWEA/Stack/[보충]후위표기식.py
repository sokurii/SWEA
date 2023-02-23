# infix : 중위표기식 문자열
# n : 중위표기식 길이

def get_postfix(infix, n):
    # 결과로 나올 후위표기식
    postfix = ""
    stack = []

    # 스택 밖에 있을때 연산자의 우선순위 (in comming priority)
    icp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 3}
    # 스택 안에 있을때 연산자의 우선순위 (in stack priority)
    isp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}

    # 문자열의 길이만큼 반복
    for i in range(n):
        # 피연산자인경우
        if "0" <= infix[i] <= "9":
            # 결과에 출력
            postfix += infix[i]
        # 연산자인경우
        else:
            # 닫는 괄호가 나오면 여는 괄호가 나올때까지 스택 안에 있는 연산자들을 꺼내서 출력
            # 괄호 안의 연산자는 먼저 계산되어야 하니까
            if infix[i] == ")":
                char = stack.pop()
                if char == "(":
                    break
                postfix += char
            # 닫는 괄호가 아니라 기타 연산자
            else:
                # 현재 연산자의 우선순위보다 스택의 top에 있는 연산자의 우선순위가 같거나 높으면 계속 pop
                # 등호의 유무에 따라서 계산 순서가 달라질수 있다. (결과는 같음)
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()

                # 그게 아니면 스택에 연산자 추가
                stack.append(infix[i])

    while stack:  # 남아있는 연산자는 모두 출력
        postfix += stack.pop()

    return postfix


def get_result(postfix):
    # 피연산자를 저장할 스택
    stack = []

    # 후위표기식에서 글자(토큰) 하나씩 떼와서 계산
    for c in postfix:

        # 피연산자는 스택에 넣기
        if "0" <= c <= "9":
            stack.append(int(c))
        # 연산자가 나오면 피연산자 두개를 꺼내서 계산한 후에 계산 결과 스택에 넣기
        else:
            right = stack.pop()  # 오른쪽이 먼저
            left = stack.pop()  # 왼쪽이 나중에

            # 연산자의 종류에 따라서 계산
            if c == "+":
                result = left + right
            elif c == "-":
                result = left - right
            elif c == "*":
                result = left * right
            elif c == "/":
                # 나누기 연산자는 결과는 실수가 된다.
                result = left / right
                # 정수 (몫만 취하고 싶을때는 // or int() 사용)

            # 이번 연산의 결과는 다음 연산자의 피연산자가 되므로 스택에 추가
            stack.append(result)

    # 마지막엔 최종 연산 결과가 스택에 단 하나 존재한다.
    # 만약 스택에 2개 이상 존재한다면 식이 잘못됬다.
    return stack.pop()


exp = "2+3*4/5"
postfix = get_postfix(exp, len(exp))

print(get_result(postfix))
