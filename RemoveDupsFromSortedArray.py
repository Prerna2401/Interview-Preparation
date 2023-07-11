class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        #for i in nums:
        #    count = nums[nums.index(i)]
        #return count
        dups = 0
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                dups += 1
            else:
                nums[i - dups] = nums[i]
        return n - dups