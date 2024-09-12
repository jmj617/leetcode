class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        answer = []
        dic = {}
        re_arr = sorted(arr)
        rank = 1
        for num in re_arr:
            if num not in dic:
                dic[num] = rank
                rank += 1
        for a in arr:
            answer.append(dic[a])
        return answer