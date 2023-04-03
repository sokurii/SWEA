'''
입력값의 개수가 정해져 있지 않다.
while문을 돌면서 입력을 받을 때마다 결과값을 출력(try)
그 이외의 값들이 들어오면 예외처리(except)
'''

while True:
    try:
        a, b = map(int,input().split())
        print(a+b)
    except:
        break