class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = 0
        for ele in nums:
            temp = temp ^ ele
        return temp