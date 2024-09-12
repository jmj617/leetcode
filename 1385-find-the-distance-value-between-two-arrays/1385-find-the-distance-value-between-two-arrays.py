class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        answer = 0
        for el in arr1:
            valid = True
        # arr2의 모든 요소와 비교
            for el2 in arr2:
                if abs(el - el2) <= d:
                    valid = False
                    break
        # 모든 조건을 만족하면 distance_value를 증가
            if valid:
                answer += 1

        return answer