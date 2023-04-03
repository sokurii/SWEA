x,y,w,h = map(int,input().split())

row = min(x,w-x)
col = min(y,h-y)

print(min(row,col))

'''
굳이 나눌 필요 없이
min(x,y,w-x,h-y)하면 되었다
'''