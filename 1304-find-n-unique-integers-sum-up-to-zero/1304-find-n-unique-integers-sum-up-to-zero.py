class Solution:
    def sumZero(self, n: int) -> List[int]:

        answer = []

        if n == 1:
            answer.append(0)
        for i in range(1, n):
            answer.append(i)
            answer.append(-i)
            if len(answer) == n:
                break
            elif len(answer) == (n - 1):
                answer.append(0)
                break
        return answer

        