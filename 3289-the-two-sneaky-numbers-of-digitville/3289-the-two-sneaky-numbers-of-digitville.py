class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        cnt = Counter(nums)
        answer = []
        for k, v in cnt.items():
            if v == 2:
                answer.append(k)
        return answer