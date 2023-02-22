T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    cheeze = list(map(int,input().split()))
    queue = []

    for i in range(N):
        c = cheeze.pop(0)
        idx = M - len(cheeze)
        queue.append([c,idx])


        while i < N:
            q = queue.pop(0)
            queue.append(q)
        print(queue)


    # for i in range(N):
    #     c = cheeze.pop(0)
    #     queue.append([c,i+1])
    #
    # n = queue.pop(0)
    # while True:
    #     if n == 1:
    #         queue[0][0] == queue[0][0]//2




    