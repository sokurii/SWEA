n =  int(input())
text = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
change = []

for i in range(n):
    if text[i] in alphabet:
        change.append(str(alphabet.index(text[i])+1))

ans = 0
for m in range(n):
    ans += int(change[m])*(31**m)

print(ans%1234567891)

'''
더 쉬운 방법 없나. . ? 시간초과 뜰 것 같다.
'''
