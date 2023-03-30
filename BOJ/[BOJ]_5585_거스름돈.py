n = 1000 - int(input())
money = [500,100,50,10,5,1]
cnt = 0

for m in money:
    cnt += n//m
    if n%m:
        n = n%m
    else:
        print(cnt)
        break


