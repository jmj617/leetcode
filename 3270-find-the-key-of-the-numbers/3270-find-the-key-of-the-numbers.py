class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        f_num1 = str(num1).zfill(4)
        f_num2 = str(num2).zfill(4)
        f_num3 = str(num3).zfill(4)
        answer = ''
        for chr_tuple in zip(f_num1, f_num2, f_num3):
            answer += min(chr_tuple)
            
        return int(answer)