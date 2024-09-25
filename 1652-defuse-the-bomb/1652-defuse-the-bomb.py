class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        answer = []
        n = len(code)
        if k == 0:
            answer = [0] * n
        else:
            for i in range(n):
                sum_num = 0
                if k > 0:
                    for j in range(1, k+1):
                        sum_num += code[(i + j) % n]
                    answer.append(sum_num)
                elif k < 0:
                    for j in range(1, -k + 1):
                        sum_num += code[(i - j) % n]
                    answer.append(sum_num)
        
        return answer