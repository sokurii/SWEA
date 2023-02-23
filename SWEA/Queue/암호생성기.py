T = 10
for tc in range(1,T+1):
    t = int(input())
    queue = list(map(int,input().split()))

    i = 1
    while True:
        if i > 5:
            i = 1
        n = queue.pop(0) -i
        if n <= 0:
            queue.append(0)
            break
        queue.append(n)
        i += 1

    print(f'#{tc}',end =' ')
    print(*queue)

    ###### 이 코드로 발표하기 ########
    # while queue[-1]!=0:
    #     for i in range(1,6):
    #         p = queue.pop(0)-i
    #         if p <= 0:
    #             p = 0
    #             queue.append(p)
    #             break
    #         queue.append(p)
    #
    # print(f'#{tc}',end=" ")
    # print(*queue)






    # n = 8
    #
    # q = [0] * (n+1) # 원형 큐 생성
    # front = rear = 0 # 0부터 시작
    # for i in range(8):
    #     rear = (rear + 1) % n
    #     q[rear] = password[rear]
    #
    # num = 1 # 1부터 차례로 증가
    #
    # while True:
    #     front +=1
    #     pw = q[front]
    #     pw -= num
    #
    #     if pw <= 0:
    #         pw = 0
    #         rear = (rear + 1) % n
    #         q[rear] = pw
    #         break
    #     else:
    #         rear +=1
    #         q[rear] = pw
    #         num +=1
    #         if num>5:
    #             num = 1
    #
    # print(f'#{tc}', end=' ')
    # for i in range(1,9):
    #     print(q[front+i],end=' ')
    # print()
    #












