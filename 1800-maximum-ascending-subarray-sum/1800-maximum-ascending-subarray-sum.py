class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sumnum = nums[0]
        maxnum = 0
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                sumnum += nums[i]
            else:
                sumnum = nums[i]
            maxnum = max(maxnum, sumnum)
            
        return maxnum