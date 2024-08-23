class Solution:
    def clearDigits(self, s: str) -> str:
        while True:  
            slist = list(s)
            digit_removed = False  

            for i in range(len(slist)):  
                if slist[i].isdigit():
                    a = slist[i-1] + slist[i]
                    s = s.replace(a, "")  
                    digit_removed = True
                    break  

            # if digit_removed == False:
            #     break
        return s
        

