class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
        rev = 0
        while x != 0:
            y = x % 10
            rev = rev*10+y
            x = x // 10
        if sign * rev < -2**31 or sign * rev > 2**31 - 1:
            return 0
        return sign*rev