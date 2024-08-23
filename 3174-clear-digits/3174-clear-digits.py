class Solution:
    def clearDigits(self, s: str) -> str:
        while True:  
            slist = list(s)
            flag = False  

            for i in range(len(slist)):  
                if slist[i].isdigit():
                    a = slist[i-1] + slist[i]
                    s = s.replace(a, "")  
                    flag = True
                    break  

            if flag == False:
                break
        return s
        

