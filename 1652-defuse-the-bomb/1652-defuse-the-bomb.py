class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        answer = []
        for i in range(len(code)):
            sum_num = 0
            if k > 0:
                for j in range(1, k+1):
                    sum_num += code[(i + j)%len(code)]
                answer.append(sum_num)
            elif k < 0:
                for j in range(1, -k + 1):
                    sum_num += code[(i - j) % len(code)]
                answer.append(sum_num)
            else:
                answer.append(0)
        
        return answer