class Solution:
    def search(self, nums: List[int], target: int) -> int:
        answer = -1
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         answer = i
        #         break
        # return answer

        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                answer = mid
                break
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return answer