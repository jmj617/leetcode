class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even = [x for x in nums if x % 2 == 0]

        if not even:
            return -1

        max_c = 0
        min_n = 0
        
        counter = Counter(even)

        for n, c in counter.items():
            if c > max_c:
                max_c = c
                min_n = n
            elif c == max_c:
                min_n = min(n, min_n)
        return min_n