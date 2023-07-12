class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        while x != 0:
            y = x % 10
            rev = rev*10+y
            x = x // 10
        return rev