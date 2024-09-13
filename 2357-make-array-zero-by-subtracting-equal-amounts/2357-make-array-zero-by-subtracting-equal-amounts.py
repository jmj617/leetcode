class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        # nums = [num for num in nums if num > 0]
        
        # while nums:
        #     minnum = min(nums)
        #     nums = [num - minnum for num in nums if num > minnum]
        #     cnt += 1
        # return cnt
        if len(nums) == 1:
            if nums[0] == 0:
                return cnt
            else:
                cnt += 1
                return cnt
        print(cnt)
        minnum = min(x for x in nums if x > 0)
        while any(nums):
            nums = [num - minnum for num in nums if num > 0]
            cnt += 1
            print(nums)
            if any(nums):
                minnum = min(x for x in nums if x > 0)
            
        return cnt

        # elements = set()
        # for num in nums:
        #     if num > 0:
        #         elements.add(num)
        # return len(elements)
