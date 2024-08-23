class Solution:
    def clearDigits(self, s: str) -> str:
        while True:  
            slist = list(s)
            digit_removed = False  

            for i in range(1, len(slist)):  
                if slist[i].isdigit():
                    a = slist[i-1] + slist[i]
                    s = s.replace(a, "", 1)  
                    digit_removed = True
                    break  

            if not digit_removed:  
                break
        return s
        

