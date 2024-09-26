class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # answer = 0
        
        # re_nums = [nums[0]]
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i-1]:
        #         re_nums.append(nums[i])
        # for i in range(1, len(re_nums) - 1):
        #     if re_nums[i-1] < re_nums[i] > re_nums[i+1]:
        #         answer += 1
        #     elif re_nums[i-1] > re_nums[i] < re_nums[i+1]:
        #         answer += 1

        # return answer

        answer = 0
        left = nums[0]
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i+1]:
                continue
            
            right = None
            for j in range(i + 1, len(nums)):
                if nums[j] != nums[i]:
                    right = nums[j]
                    break
            
            if right is not None:
                if (left < nums[i] > right) or (left > nums[i] < right):
                    answer += 1
            
            left = nums[i]
        
        return answer