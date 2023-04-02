lst = list(map(int,input().split()))

cnt = 0
for i in range(1,8):
    if lst[i-1] == lst[i]-1:
        cnt += 1
    elif lst[i-1] == lst[i]+1:
        cnt -= 1
    else:
        cnt = 0

if cnt == 7:
    print('ascending')
elif cnt == -7:
    print('descending')
else:
    print('mixed')

'''
좀. . 너무 단순하게 풀었는데
더 좋은 방법이 있지 않을까? 
'''


