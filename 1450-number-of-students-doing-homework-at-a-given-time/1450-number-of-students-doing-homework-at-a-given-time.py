class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        answer = 0
        
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and queryTime<=endTime[i]:
                answer += 1
        return answer
