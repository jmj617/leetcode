class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))  # 단어를 정렬
            dic[sorted_word].append(word)  # 정렬된 단어를 키로 사용하여 같은 단어 묶음 생성

        # 정답 리스트로 변환
        answer = list(dic.values())
        return answer