class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s = ''
        idx = word.find(ch)
        if ch not in word:
            return word
        for i in range(len(word)):
            s += word[i]
            if i == idx:
                s = s[::-1]
        
        return s
        