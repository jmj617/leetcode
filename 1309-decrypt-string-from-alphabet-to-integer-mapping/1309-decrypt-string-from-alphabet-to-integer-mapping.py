class Solution:
    def freqAlphabets(self, s: str) -> str:
        sdict = {}
        slist = []
        for i in range(1, 27):
            if i < 10:
                sdict[str(i)] = chr(i + 96)
            else:
                sdict[str(i)+'#'] = chr(i + 96)
        
        j = 0
        while j < len(s):
            if j+2 < len(s) and s[j+2] == '#':
                slist.append(sdict[s[j:j+3]])
                j += 3
            else:
                slist.append(sdict[s[j]])
                j += 1
        
        # answer = ''
        # for ch in slist:
        #     answer += sdict[ch]
        print(slist)

        return ''.join(slist)