def climbStairs(self, n: int) -> int:
        lst = [1,1]
        for i in range(2, n+1):
            lst.append(lst[i-1]+lst[i-2])
        return lst[n]