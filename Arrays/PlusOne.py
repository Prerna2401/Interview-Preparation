class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for ele in digits:
            ele = str(ele)
            s += ele
        s = int(s)
        s += 1
        s = str(s)
        final = []
        for ele in s:
            ele = int(ele)
            final.append(ele)
        return final