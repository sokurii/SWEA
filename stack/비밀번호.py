T = 10

for tc in range(1,T+1):
    n, N = input().split()
    lst = []

    for i in N:
        if len(lst)==0:
            lst.append(i)
        elif len(lst)!=0:
            if i == lst[-1]:
                lst.pop()
            else:
                lst.append(i)
    print(f'#{tc}', end=' ' )
    print(*lst,sep='')