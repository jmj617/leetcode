class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        answer = 0
        
        re_nums = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                re_nums.append(nums[i])
        for i in range(1, len(re_nums) - 1):
            if re_nums[i-1] < re_nums[i] > re_nums[i+1]:
                answer += 1
            elif re_nums[i-1] > re_nums[i] < re_nums[i+1]:
                answer += 1

        return answer