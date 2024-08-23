class Solution:
    def addDigits(self, num: int) -> int:
        
        # cnt = 0
        # if num > 0 and num < 10:
        #     cnt = 1
        
        while num >= 10:
            a = 0
            s = str(num)
            
            for i in range(len(s)):
                a += int(s[i])
            num = a
        
        return num