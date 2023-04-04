while True:
    num = input()
    if num == '0':
        break

    reverse = ''
    for i in range(len(num)-1,-1,-1):
        reverse += num[i]

    if num == reverse:
        print('yes')
    else:
        print('no')





