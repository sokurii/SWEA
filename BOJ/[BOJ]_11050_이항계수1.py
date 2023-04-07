n,k = map(int,input().split())
if k == 0 :
    print(1)
else:
    for i in range(n-1,n-k,-1):
        n *= i
    for j in range(k-1,0,-1):
        k *= j
    print(n // k)

'''
첫 시도에서 런타임에러(ZeroDivisionError)가 떴는데
분모가 되는 k의 범위가 0 이상이라서 0으로 나누는 경우를 생각하지 못했다.
k가 0일 때의 조합은 아무것도 안뽑는 경우의 수이므로 1 출력 
'''






