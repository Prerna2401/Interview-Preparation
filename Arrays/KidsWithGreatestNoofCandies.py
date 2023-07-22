class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        n = len(candies)
        a = []
        for i in range(n):
            check = candies[i] + extraCandies
            #print(check)
            a.append(check >= maxi)
            #print(a)
            check = 0
        return a