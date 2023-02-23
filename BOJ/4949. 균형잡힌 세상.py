while True:
    text = input()
    stack = []

    if text == '.':     # '.'이 있으면 종료
        break

    for t in text:
        if t in '([':   # 여는 괄호가 있으면 스택에 push
            stack.append(t)

        # 닫는 괄호라면 경우에 따라 처리
        elif t == ']':
            if stack and stack[-1] == '[':  # 스택에 남아 있고 마지막 글자가 짝이면
                stack.pop()                 # 스택에서 제거
            else:                           # 스택에 남아있지 않거나, 마지막 글자가 다른 짝이면
                stack.append(t)             # 스택에 push
                break                       # 이미 균형이 깨졋으므로 종료

        elif t == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(t)
                break

    if stack:           # 순회가 끝나고 스택에 남아 있으면
        print('no')     # 균형을 이루지 않으므로 'no'
    else:               # 스택에 아무것도 남아 있지 않으면
        print('yes')    # 균형을 이루므로 'yes'