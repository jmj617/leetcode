class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        minnum = min(nums)
        cnt = 0
        while sum(nums) > 0:
            nums = [x - 1 for x in nums]
            minnums = min(nums)
            cnt += 1
        return cnt