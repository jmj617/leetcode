class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sen = sentence.split(' ')
        # print(sen)
        for i in range(len(sen)):
            n = len(searchWord)
            if searchWord == sen[i][:n]:
                return i+1
        return -1
