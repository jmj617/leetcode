class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        answer = 0
        
        # for i in range(len(startTime)):
        #     if startTime[i] <= queryTime and queryTime<=endTime[i]:
        #         answer += 1
        # return answer

        for start, end in zip(startTime, endTime):
            if start <= queryTime and queryTime <= end:
                answer += 1
        return answer