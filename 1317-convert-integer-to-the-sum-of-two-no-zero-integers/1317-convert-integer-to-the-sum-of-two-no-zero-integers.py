class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        answer = []
        for i in range(1, n):
            j = n-i
            if '0' in str(j) and '0' in str(i):
                continue
            else:
                answer.append(i)
                answer.append(j)
                break
            
        
        return answer
        