class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        nums = [num for num in nums if num > 0]  # 0 제거
        
        while nums:
            min_num = min(nums)
            nums = [num - min_num for num in nums if num > min_num]
            cnt += 1
        return cnt

        # elements = set()
        # for num in nums:
        #     if num > 0:
        #         elements.add(num)
        # return len(elements)
