class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reverse = int(str(num)[::-1])
        answer = False
        re_reverse = str(reverse)[::-1]
        if int(re_reverse) == num:
            answer = True
        return answer