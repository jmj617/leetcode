class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even = [x for x in nums if x % 2 == 0]

        if not even:
            return -1
        
        maxn = 0
        answer = -1
        counter = Counter(even) 
        for n, c in counter.items():
            if c > maxn:
                maxn = c
                answer = n
            elif c == maxn:
                answer = min(n, answer)
        
        return answer