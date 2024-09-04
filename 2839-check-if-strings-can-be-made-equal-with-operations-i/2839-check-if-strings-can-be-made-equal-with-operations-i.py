class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        answer = False
        s11 = sorted([s1[0], s1[2]])
        s12 = sorted([s1[1], s1[3]])

        s21 = sorted([s2[0], s2[2]])
        s22 = sorted([s2[1], s2[3]])
        
        if s11 == s21 and s12 == s22:
            answer = True

        

        return answer