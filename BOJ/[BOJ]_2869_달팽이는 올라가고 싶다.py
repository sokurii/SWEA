A,B,V = map(int,input().split())

d = (V-B)/(A-B)

if d == int(d):
    print(int(d))
else:
    print(int(d)+1)
'''
간단한 수학식으로 풀어보자면
A*d - B*(d-1) = V
이를 d에 대해 정리하면 위와 같은 식이 나온다
'''


# day = 1
# while True:
#     V -= A
#     if V <= 0:
#        print(day)
#        break
#     else:
#         V += B
#         day +=1







