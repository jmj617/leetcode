class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even = [x for x in nums if x % 2 == 0]

        if not even:
            return -1
        
        counter = Counter(even)
        return min(counter, key=lambda x: (-counter[x], x))