stri = input()
print(stri)
n = len(stri)
freq = [0 for i in range(26)]
for i in range(n):
    if stri[i] != ' ':
        freq[ord(stri[i]) - ord('a')] += 1
    else:
        continue
for i in range(n):
    if stri[i] != ' ':
        if freq[ord(stri[i]) - ord('a')] != 0:
            print(stri[i],freq[ord(stri[i]) - ord('a')], end = ' ')
            freq[ord(stri[i]) - ord('a')] = 0