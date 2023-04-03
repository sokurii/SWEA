word = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
ans = []

for i in range(26):
    if alphabet[i] in word:
        ans.append(word.index(alphabet[i]))
    else:
        ans.append(-1)
print(*ans)

