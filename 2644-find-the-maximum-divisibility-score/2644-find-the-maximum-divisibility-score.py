class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        cnt_num = {}

        for div in divisors:
            cnt = 0
            for num in nums:
                if num % div == 0:
                    cnt += 1
            cnt_num[div] = cnt
        
        cnt_num = sorted(cnt_num.items(), key=lambda x: (-x[1], x[0]))

        
        return cnt_num[0][0]
        