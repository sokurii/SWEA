T = 10

for tc in range(1,T+1):
    n = int(input())
    s = input()
    text = input()

    lst = []
    if s in text:
        lst.append(s)
    print(len(lst))
