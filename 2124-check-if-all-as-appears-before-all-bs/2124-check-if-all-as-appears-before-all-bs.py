class Solution:
    def checkString(self, s: str) -> bool:
        a = 0
        b = 0
        answer = True
        ab = False
        for i in range(len(s)):
            if s[i] == 'a':
                a = i
            elif s[i] == 'b':
                b = i
            if a != 0 and b != 0:
                ab = True
            if ab == True and b < a:
                answer = False
                break
        
        return answer
            