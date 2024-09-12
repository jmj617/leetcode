class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        answer = 0
        for el in arr1:
            valid = 0
            for el2 in arr2:
                if abs(el - el2) > d:
                    valid += 1
            if valid == len(arr2):
                answer += 1

        return answer