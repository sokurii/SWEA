n = int(input())
lst = list(map(int,input().split()))

mx = max(lst)
for i in range(n):
    lst[i] = lst[i]/mx*100

print(sum(lst)/n)
