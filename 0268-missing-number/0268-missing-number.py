class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        compare = [x for x in range(n+1)]
        for i in range(0, n+1):
            if compare[i] not in nums:
                answer = compare[i]
        return answer