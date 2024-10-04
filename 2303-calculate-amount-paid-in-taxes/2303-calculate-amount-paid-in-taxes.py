class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        n = []
        answer = 0
        prev = 0

        for upper, percent in brackets:
            if upper <= income:
                amount = upper - prev
                answer += amount * (percent / 100)
            else:
                amount = income - prev
                answer += amount * (percent / 100)
                break
            prev = upper

        return answer
