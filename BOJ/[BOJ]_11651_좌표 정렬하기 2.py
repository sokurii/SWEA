import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    x,y=map(int,input().split())
    lst.append((x,y))

lst.sort(key=lambda x: (x[1],x[0]))

for t in lst:
    print(*t)

'''
드디어 람다 쓰는 방법을 조금 터득했다.
근데 시간이 엄청 오래 걸린다.
시간복잡도 계산하는 방법을 다시 공부해야겠다.

import sys
input = sys.stdin.readline
이렇게 받으면 시간 복잡도 줄어듦 
'''