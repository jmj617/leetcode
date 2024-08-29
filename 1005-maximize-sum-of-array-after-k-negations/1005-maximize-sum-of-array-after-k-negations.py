class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 1. 음수 개수랑 k 비교
        # 2. 음수 < k -> 음수를 다 하나씩 양수로 바꾼 다음에 제일 작은수 음수로 변환
        # 3. 음수 > k -> 절대값이 제일 큰 음수 변경
        # n_cnt = sum(1 for num in nums if num < 0)
        # cnt = 0
        # answer = 0
        # if n_cnt <= k:
        #     for i in range(len(nums)):
        #         if nums[i] < 0:
        #             nums[i] = -nums[i]
        #     k -= n_cnt
        #     if k % 2 == 0:
        #         answer = sum(nums)
        #     else:
        #         min_n = min(nums)
        #         for j in range(len(nums)):
        #             if nums[j] == min_n:
        #                 nums[j] = -nums[j]
        #                 break
        #         answer = sum(nums)
        # else:
        #     sorted_nums = sorted(nums)
        #     for i in range(len(sorted_nums)):
        #         if k == 0:
        #             break
        #         sorted_nums[i] = -sorted_nums[i]
        #         k -= 1

        #     answer = sum(sorted_nums)
        # return answer

        # Step 1: 음수와 양수의 개수를 세고, nums를 절대값 기준으로 정렬
        nums.sort(key=lambda x: abs(x), reverse=True)

        # Step 2: 가장 큰 절대값의 음수를 K번 양수로 변환
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1

        # Step 3: 변환이 끝난 후 남은 K가 홀수라면, 가장 작은 값 하나를 다시 음수로 변환
        if k % 2 == 1:
            nums[-1] = -nums[-1]

        # Step 4: 최종 리스트의 합을 계산하여 반환
        return sum(nums)