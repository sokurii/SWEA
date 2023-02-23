# 후위표기식 계산
def get_result(postfix):
    stack = []

    # 후위표기식에서 글자(토큰)하나씩 계산
    for c in postfix:
        # 피연산자이면 스택에 쌓기
        if '0'<= c <= '9':
            stack.append(int(c))
        # 연산자이면
        else:
            # pop 해주기 전에 피연산자 개수 부족하면 에러
            if len(stack) <2:
                return 'error'
            right = stack.pop()
            left = stack.pop()

            # 연산자 종류에 따라 계산
            if c == '+':
                result = left + right
            elif c =='-':
                result = left - right
            elif c == '*':
                result = left *right
            elif c == '/':
                result = left // right

            stack.append(result)
