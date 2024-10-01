class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {} 

        for word in strs:
            word2 = ''.join(sorted(word))
            print(word2)
            if word2 not in dic:
                dic[word2] = []
            dic[word2].append(word)
        return dic.values()