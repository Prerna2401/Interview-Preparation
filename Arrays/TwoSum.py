class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        #for i in range(n):
        #    for j in range(i, n):
        #        if nums[i] + nums[j] == target:
        #            return[i,j]
        k = 0
        for i in nums:
            j = target - i
            k += 1
            temp = nums[k:]
            if j in temp:
                return[k-1, temp.index(j)+k]