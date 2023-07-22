class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)
        def gcd(a,b):
            if a == 0:
                return b
            if b == 0:
                return a
            if a == b:
                return a
            if a > b:
                return gcd(a-b,b)
            return gcd(a,b-a)

        common = gcd(n1,n2)
        #print(common)
        res = ''
        for i in range(common):
            res += str1[i]
        if str1 + str2 == str2 + str1:
            return res
        else:
            return ''