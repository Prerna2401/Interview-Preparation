class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        s = ''
        i = 0
        while i < n1 or i < n2:
            if i < n1:
                s += word1[i]
            if i < n2:
                s += word2[i]
            i += 1
        return s