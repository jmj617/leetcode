class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr2 = {}
        for ar in arr:
            if ar not in arr2:
                arr2[ar] = 1
            else:
                arr2[ar] += 1
        cnt = 0
        for key, v in arr2.items():
            if v == 1:
                cnt += 1
                if cnt == k:
                    return key
        return "" 