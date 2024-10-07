class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        
        total = 0

        for i in range(len(s)):
            if i != (len(s)-1) and s[i] == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                num = - symbol[s[i]]
                total += num

            elif i != (len(s)-1) and s[i] == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                num = - symbol[s[i]]
                total += num


            elif i != (len(s)-1) and s[i] == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                num = - symbol[s[i]]
                total += num

            else:
                total += symbol[s[i]]
            print(f"{i}", total)
        
        
        
        
        
        return total