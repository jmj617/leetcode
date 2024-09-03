class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        f_num1 = str(num1).zfill(4)
        f_num2 = str(num2).zfill(4)
        f_num3 = str(num3).zfill(4)
        answer = ''
        for n1, n2, n3 in zip(f_num1, f_num2, f_num3):
            answer += str(min(int(n1), int(n2), int(n3)))
        return int(answer)