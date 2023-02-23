import sys
n = int(sys.stdin.readline())
stack =[]
for _ in range(n):
    text = sys.stdin.readline().split()

    if text[0] == 'push':
        stack.append(int(text[1]))

    elif text[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif text[0] == 'size':
        print(len(stack))

    elif text[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)