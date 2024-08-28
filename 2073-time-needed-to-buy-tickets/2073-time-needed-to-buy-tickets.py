class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        answer = 0

        while tickets[k]>0:
            for i in range(len(tickets)):
                if tickets[i] == 0:
                    continue
                tickets[i] -= 1
                answer += 1
                if tickets[k] == 0:
                    break
        return answer
            
