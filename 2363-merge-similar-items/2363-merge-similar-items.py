class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dict1 = {}
        for i, j in items1:
            dict1[i] = j
        for k, l in items2:
            if k in dict1.keys():
                dict1[k] += l
            else:
                dict1[k] = l
        answer = []
        for key in sorted(dict1.keys()):
            answer.append([key, dict1[key]])
        return answer