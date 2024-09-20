class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        # inc_len, dec_len = 1, 1 
        # max_len = 1
        
        # for i in range(1, len(nums)):
        #     if nums[i] > nums[i - 1]:
        #         inc_len += 1 
        #         dec_len = 1
        #     elif nums[i] < nums[i - 1]:
        #         dec_len += 1
        #         inc_len = 1
        #     else:
        #         inc_len = dec_len = 1
            
        #     max_len = max(max_len, inc_len, dec_len)
        
        # return max_len
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