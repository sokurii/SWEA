T = int(input())
for tc in range(1,T+1):
    text = input()
    text_lst = []

    for i in text:

        if len(text_lst) == 0 and i in '({})':
            text_lst.append(i)

        elif len(text_lst) != 0:  # 리스트에 요소가 존재할 때
            if i == '(' :
                text_lst.append(i)

            if i == '{' :
                text_lst.append(i)

            if i == ')' :
                if text_lst[-1] == '(': # 짝이 맞으면 마지막 요소 제거
                    text_lst.pop()
                else:
                    text_lst.append(i)

            if i == '}':
                if text_lst[-1] == '{':
                    text_lst.pop()
                else:
                    text_lst.append(i)

    if len(text_lst) == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')









