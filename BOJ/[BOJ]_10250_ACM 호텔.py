# N = int(input())
# for _ in range(N):
#     H,W,N = map(int,input().split())
#     floor, num = 0,0
#
#     if N%H:
#         floor = str(N%H)
#         num = str(N//H+1)
#     else:
#         floor = str(H)
#         num = str(N//H)
#
#     if int(num) < 12:
#         num = num.zfill(2)
#
#     print(floor+num)

'''
굳이굳이 문자형,정수형으로 바꿔가며 풀었다.
층수에 *100 + 호수 해주면 됨 ㄱ-
'''

'''
N = int(input())
for _ in range(N):
    H,W,N = map(int,input().split())
    floor, num = 0,0

    if N%H:
        floor = N%H
        num = N//H+1
    else:
        floor = H
        num = N//H

    print(floor*100+num)
'''
