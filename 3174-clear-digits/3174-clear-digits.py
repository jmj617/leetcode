class Solution:
    def clearDigits(self, s: str) -> str:
        slist = list(s)
        num = 0
        for i in range(len(slist)):
            if slist[i].isdigit():
                num += 1
        if num == 0:
            return s
        else:
            while True:
                slist = list(s)
                digit_removed = False
                for i in range(len(slist)):
                    if slist[i].isdigit():
                        a = slist[i-1] + slist[i]
                        print(a)
                        s = s.replace(a, "", 1)
                        print(s)
                        digit_removed = True
                if not digit_removed:  
                    break
        return s
        

