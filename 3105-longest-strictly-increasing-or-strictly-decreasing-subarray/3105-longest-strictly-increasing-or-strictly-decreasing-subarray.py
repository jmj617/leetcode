class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            answer = 1
        inc = 1
        dec = 1
        answer = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                inc += 1
                dec = 1
            elif nums[i-1] > nums[i]:
                inc = 1
                dec += 1
            else:
                inc = 1
                dec = 1
            answer = max(answer, inc, dec)
        return answer